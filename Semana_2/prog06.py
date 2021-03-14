# coding=utf-8
# Condicionais e Booleanos - If, Else, e Elif

language = 'Python'

if True: #Condição if colocada arbitrariamente como verdadeira
    print('Condition is True')

if language == 'Python': #Condição if que checa um método de comparação. Qualquer método de comparação pode ser usado
    print('language is Python')
elif language == 'Java': #Condição elif que também faz uma comparação com a variável languege
    print('language is Java')
elif language == 'C++':
    print('language is C++')
else: #Caso todas as comparações sejam falsas o bloco dentro de else será executado
    print("language undefined")

user = 'Adm'
logged_in = True

if user == 'Adm' and logged_in: #Teste usando and, que checa se as duas premissas são verdadeiras.
    print('Admin on system')
elif user == 'Adm' and not logged_in: #Teste usando not, que checa se a informação é falsa. Se a COMPARAÇÃO for FALSA a PREMISSA usando NOT é VERDADEIRA.
    print('Login requested for Admin')
elif user != 'Adm' and logged_in or not logged_in: #Teste usando or checando as duas premissas. Se PELO MENOS uma for VERDADEIRA a SENTENÇA é VERDADEIRA também. 
    print('User undefined!\nCall denied.')

a = [1, 2, 3] #Criação de uma lista a.
b = [1, 2, 3] #Criação de uma lista b.
c = a #Criação de uma lista c de valores iguais e com a mesma identidade de a (são a mesma lista).

print(a == b) #Compara os valores das listas e retorna verdadeiro se eles forem iguais.
print(a is b) #Compara a identidade das listas (local armazenado na memória) e retorna verdadeiro se for a mesma
print(id(a), id(b)) #Print das identidades de a e b.
print(a is c)

#Exemplos de situações em que a condição if entenderá como FALSO

teste = False #Booleanos falsos
name = '' #Strings, listas, tupples, sets e diocionários vazios
lst = []
dic = {}
st = set()
num = 0 #Tipos numéricos zerados
num_float = 0.0