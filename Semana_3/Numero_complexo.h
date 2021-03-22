#include <iostream>
#include <cmath>

class Numero_complexo{
    private:
        float parte_real;
        float parte_imaginaria;

    public:
        Numero_complexo(float _parte_real, float _parte_imaginaria);
        void exibe();
        void emPolar();
        float getReal();
        float getImaginaria();
        Numero_complexo somaCom(Numero_complexo num);
        Numero_complexo subtracaoCom(Numero_complexo num);
        Numero_complexo multiplicacaoCom(Numero_complexo num);
        Numero_complexo divisaoCom(Numero_complexo num);

};


Numero_complexo::Numero_complexo(float _parte_real, float _parte_imaginaria){
    parte_real = _parte_real;
    parte_imaginaria = _parte_imaginaria;
}

void Numero_complexo::exibe(){
    std::cout << "z = " << parte_real << " + " << parte_imaginaria << "i" << std::endl;
}

void Numero_complexo::emPolar(){
    double z_polar = sqrt(pow(parte_real, 2) + pow(parte_imaginaria, 2));
    double teta = atan(parte_imaginaria/parte_real) * 180 / 3.14159265;
    std::cout << "z = " << z_polar << "|" << teta << "°" << std::endl;
}

float Numero_complexo::getReal(){
    return parte_real;
}

float Numero_complexo::getImaginaria(){
    return parte_imaginaria;
}

Numero_complexo Numero_complexo::somaCom(Numero_complexo num){
    float novo_real = parte_real + num.getReal();
    float novo_imaginario = parte_imaginaria + num.getImaginaria();
    return Numero_complexo(novo_real, novo_imaginario);
}

Numero_complexo Numero_complexo::subtracaoCom(Numero_complexo num){
    float novo_real = parte_real - num.getReal();
    float novo_imaginario = parte_imaginaria - num.getImaginaria();
    return Numero_complexo(novo_real, novo_imaginario);
}

Numero_complexo Numero_complexo::multiplicacaoCom(Numero_complexo num){
    float novo_real = parte_real * num.getReal();
    float novo_imaginario = parte_imaginaria * num.getImaginaria();
    return Numero_complexo(novo_real, novo_imaginario);
}

Numero_complexo Numero_complexo::divisaoCom(Numero_complexo num){
    float novo_real = parte_real / num.getReal();
    float novo_imaginario = parte_imaginaria / num.getImaginaria();
    return Numero_complexo(novo_real, novo_imaginario);
}