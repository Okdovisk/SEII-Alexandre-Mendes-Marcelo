#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
#include <string>

using namespace std;

int main(){
    // Creat a socket
    int client = socket(AF_INET, SOCK_STREAM, 0);
    if(client < 0){
        cerr << "Creating the socket ERROR." << endl;
        return -1;
    }

    cout << "Creat socket sucefully." << endl;

    // Creat a hint structure for the server we've gonna connect with
    int portNum = 54000;
    string ipadress = "127.0.0.1"; 

    sockaddr_in hint;
    hint.sin_port = htons(portNum);
    hint.sin_family = AF_INET;
    inet_pton(AF_INET, ipadress.c_str(), &hint.sin_addr);

    // Connect to the server on the socket
    int connectRes = connect(client, (sockaddr*)&hint, sizeof(hint));
    if(connectRes < 0){
        cerr << "Connection FAIL." << endl;
        return -2;
    }

    cout << "Connected!" << endl;

    // While loop:
    char buffer[4096];
    string userInput;

    do{
        //     Enter lines of test
        cout << "> ";
        getline(cin, userInput);

        //     Send to server
        int sendRes = send(client, userInput.c_str(), userInput.size() + 1, 0);
        if(sendRes < 0){
            cerr << "Send message ERROR.\r\nTry again!" << endl;
            continue;
        }

        //     Wait for response
        /*memset(buffer, 0, sizeof(buffer));
        int bytesReceived = recv(client, buffer, sizeof(buffer), 0);
        if(bytesReceived < 0){
            cerr << "Reciev message ERROR." << endl;
            continue;
        }
        

        //     Display response
        cout << "Server: " << string(buffer, bytesReceived) << "\r\n";*/
    }while(true);

    // Close socket
    close(client);


    return 0;
}