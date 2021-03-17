# coding=utf-8

#Organizando listas, tupples e objetos.

li = [9, 1, 6, 3, 8, 4, 8, 7, 2, 5] #Uma lista de números de 1 a 9 em ordem aleatória.
di = {'Name':'Von Neumann', 'Age':'Immortal', 'Job':'Change the world'} #Dicionário com chaves e valores.
li_negative = [-5, -2, -1, 0, 3, 4] #Lista com valores negativos

s_li = sorted(li) #Função para organizar os elementos da lista em ordem crescente e salvar a nova ordem na variável.

print('Sorted list(s_li):\t{}'.format(s_li))
print('Normal list(li):\t{}'.format(li))

li.sort() #Método para organizar em ordem crescente os elementos da lista, mas, diferente da função, não há retorno de uma lista nova.

#ATENÇÃO!: O método sorted aceita somente listas em sua execução, já a função pode ser aplicada até mesmo em tupples. O que faz sentido, visto que ela não aletera a variável raiz, ela cria uma nova.

print('Sorted metod(li):\t{}'.format(li))

li.sort(reverse=True) #Tanto o método quanto a função podem organizar os elementos em órdem decrescente, basta passar 'reverse=True' como parâmetro no método ou como segundo parâmetro na função.

print('Reverse sorted(li):\t{}'.format(li))

s_di = sorted(di) #A função sorted organiza os dicionários baseado em suas chaves.

print('Sorted dictionary:\t{}'.format(s_di))

s_li_negative = sorted(li_negative, key=abs) #Com key=abs os valores da lista são lidos como absolutos, ou seja, os negativos são considerados positivos e depois a função organiza os elementos.

print('Sorted with key:\t{}'.format(s_li_negative))
print('\n\n')

class Employee(): #Classe que cria a abstração de empregados com os atributos nome, idade e salário.
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carlos', 20, 10000) #Criação de 3 empregados fictícios.
e2 = Employee('Samantha', 23, 12500)
e3 = Employee('Roger', 30, 5000)

employees = [e1, e2, e3] #Lista contendo os empregados e seus atributos.

#ATENÇÃO:A função não sabe qual tipo de ordenação ela deve fazer caso não seja especificado de alguma forma. Para isso existem algumas maneiras.
#1) É possível criar uma função específica e local que define qual atributo será usado para organizar a lista.
#2) Criar uma mini função anônima 'lambda' que captura o atributo especificado.
#3) Importar uma função 'attrgetter' de 'operator' que busca nos dados o atributo especificado.
print('Formas de pegar atributos específicos da classe Employee')
#1ª Forma de definir o atributo a ser considerado:
def e_atr(emp):
    return emp.name #Basta alterar 'name' para o atributo que deseja levar em consideração.

s1_employees = sorted(employees, key=e_atr)
print('1ª Forma:\t{}'.format(s1_employees))

#2ª Forma de definir o atributo a ser considerado:
s2_employees = sorted(employees, key=lambda e: e.age)
print('2ª Forma:\t{}'.format(s2_employees))

#3ª Forma de definir o atributo a ser considerado:
from operator import attrgetter 
s3_employees = sorted(employees, key=attrgetter('salary'))
print('3ª Forma:\t{}'.format(s3_employees))
