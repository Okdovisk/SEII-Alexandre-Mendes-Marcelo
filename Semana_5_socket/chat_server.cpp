#include <iostream>
#include <sys/types.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
#include <string>


using namespace std;

int main(){
    //Creat a socket
    int listening = socket(AF_INET, SOCK_STREAM, 0);
    if(listening < 0){
        cerr << "Creating a socket ERROR." << endl;
        return -1;
    }

    cout << "Creat socket sucefully." << endl;

    //Bind a socket to an IP/Port
    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(54000);
    inet_pton(AF_INET, "0.0.0.0", &hint.sin_addr);

    if(bind(listening, (sockaddr*)&hint, sizeof(hint)) < 0){
        cerr << "Binding socket ERROR." << endl;
        return -2;
    }

    cout << "Bind done." << endl;

    //Mark the socket for listening in
    if(listen(listening, SOMAXCONN) < 0){
        cerr << "Can't listen." << endl;
        return -3;
    }

    //Accept a call
    sockaddr_in client;
    socklen_t clientSize;
    char host[NI_MAXHOST];
    char svc[NI_MAXSERV];

    int clientSocket = accept(listening, (sockaddr*)&client, &clientSize);

    if(clientSocket < 0){
        cerr << "Problem with client." << endl;
        return -4;
    }

    cout << "Client accepted." << endl;

    //Close listening socket
    close(listening);

    memset(host, 0, NI_MAXHOST);
    memset(svc, 0, NI_MAXSERV);

    int result = getnameinfo((sockaddr*)&client, sizeof(client), host, NI_MAXHOST, svc, NI_MAXSERV, 0);

    if(result){
        cout << host << " connected on " << svc << endl;
    }
    else{
        inet_ntop(AF_INET, &client.sin_addr, host, NI_MAXHOST);
        cout << host << " connected on " << ntohs(client.sin_port) << endl;
    }

    //While reciebing - display messages and echo messages
    char buffer[4096];
    while (true){
        //Clear buffer
        memset(buffer, 0, sizeof(buffer));

        //Wait for a message
        int bytesRecv = recv(clientSocket, buffer, sizeof(buffer), 0);
        if(bytesRecv < 0){
            cerr << "There was a connection issue." << endl;
            break;
        }
        if(bytesRecv == 0){
            cout << "Client desconnected." << endl;
            break;
        }

        //Display message
        cout << "Recieved(" << host << "): " << string(buffer, 0, bytesRecv) << endl;

        //Resend message
        //send(clientSocket, buffer, bytesRecv + 1, 0);
    }
    //Close socket
    close(clientSocket);

    return 0;
}