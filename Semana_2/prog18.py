# coding=utf-8

#Escopo de variáveis-Compreendendo a regra LEGB e declarações globais/não locais.
# LEGB = Local, Enclosing, Global e Built-in

x = 'global_x' #Variável declarada globalmente

def test():
    y = 'local_y' #Variável declarada localmente. Ou seja, ela só pode ser acessada dentro do escopo em que foi feita, dentro da função test().
    print(y)
    print(x) #Esse print funciona pois x se enquadra no 3 tipo da busca pelo valor da variável. Ela foi declarada globalmente, então pode ser acessada nessa região.

test()
print(x)

def test_x():
    x = 'local_x'
    print(x) #Por mais que existam duas variáveis com o mesmo nome 'x', o sistema de procura usa a primeira variável encontrada a partir da órdem de busca, que é o nível local.

test_x()
print(x) #Como a variável local em test_x() não pertence além daquele escopo, esse print usa a variável global.

def test_x_overwriting():
    global x #Essa chamada trás a variável global para dentro do escopo local de test_x_overwriting(), então ela passa a ser usada na função e pode ser sobrescrita ao mudar o valor de x.
    x = 'local_x'
    print(x)

test_x_overwriting() #Agora tanto a função quanto o print se referem à mesma variável.
print(x)

def test_z(z): #Cria a variável z, que recebe seu conteúdo pela chamada da função.
    print(z) #Essa variável é local.

test_z('local_z\n') #Passa o conteúdo da varíável para a função.

def outer():
    k = 'outer_k' #Cria uma variável local k.

    def inner():
        #nonlocal k #Colocando 'nonlocal k' faria o código buscar uma variável k não local para trabalhar, que seria a k cujo valor é 'outer_k'. Assim, esse copo manipularia essa variável específica.
        k = 'inner_k' #Também cria uma variável local k.
        print(k) #O print em questão corresponde à variável k mais próxima referente a LEGB. Ou seja, o k local cujo valor é 'inner_k'. Não houvesse esse k local, o outro mais próximo seria buscado, sendo ele 'outer_k'

    inner()
    print(k)

outer()
