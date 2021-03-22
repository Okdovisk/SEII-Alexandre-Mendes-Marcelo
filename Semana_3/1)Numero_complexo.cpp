#include <iostream>
#include "Numero_complexo.h"

using namespace std;

int main(){
    Numero_complexo primeiro_numero = Numero_complexo(1, 1);
    Numero_complexo segundo_numero = Numero_complexo(10,22);
    primeiro_numero.exibe();
    segundo_numero.exibe();
    primeiro_numero.emPolar();
    segundo_numero.emPolar();

    cout << "Primeiro número, parte real: " << primeiro_numero.getReal() << endl;
    cout << "Primeiro número, parte imaginária(i): " << primeiro_numero.getImaginaria() << endl;
    cout << "Segundo número, parte real: " << segundo_numero.getReal() << endl;
    cout << "Segundo número, parte imaginária(i): " << segundo_numero.getImaginaria() << endl << endl << endl;

    Numero_complexo terceiro_numero = primeiro_numero.somaCom(segundo_numero);

    cout << "Parte real da soma: " << terceiro_numero.getReal() << endl;
    cout << "Parte imaginária(i) da soma: " << terceiro_numero.getImaginaria() << endl << endl;

    Numero_complexo quarto_numero = primeiro_numero.subtracaoCom(segundo_numero);

    cout << "Parte real da subtração: " << quarto_numero.getReal() << endl;
    cout << "Parte imaginária(i) da subtração: " << quarto_numero.getImaginaria() << endl << endl;

    Numero_complexo quinto_numero = primeiro_numero.multiplicacaoCom(segundo_numero);

    cout << "Parte real da multiplicação: " << quinto_numero.getReal() << endl;
    cout << "Parte imaginária(i) da multiplicação: " << quinto_numero.getImaginaria() << endl << endl;

    Numero_complexo sexto_numero = primeiro_numero.divisaoCom(segundo_numero);

    cout << "Parte real da divisão: " << sexto_numero.getReal() << endl;
    cout << "Parte imaginária(i) da divisão: " << sexto_numero.getImaginaria() << endl << endl;

    return 0;
}