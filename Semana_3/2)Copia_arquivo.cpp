#include <iostream>

using namespace std;

int main(int arg_c, char* arg_v[]){
    FILE* arquivo = fopen(arg_v[1], "rb");

    fseek(arquivo, 0, SEEK_END);
    int quantidade_de_elementos = ftell(arquivo);
    rewind(arquivo);

    size_t* copia_memoria = new(nothrow) size_t[quantidade_de_elementos];
    if(!copia_memoria){
        cout << "Falha na alocação de memória!" << endl;
        return -1;
    }

    int check = fread(copia_memoria, 1, quantidade_de_elementos, arquivo);
    if(check != quantidade_de_elementos){
        cout << "Erro na leitura." << endl;
        return -1;
    }

    FILE* copia_binaria = fopen(arg_v[2], "wb");

    int check2 = fwrite(copia_memoria, 1, quantidade_de_elementos, copia_binaria);
    if(check2 != quantidade_de_elementos){
        cout << "Falha na escrita." << endl;
        return -1;
    }

    delete copia_memoria;
    fclose(arquivo);
    fclose(copia_binaria);
    return 0;
}