# coding=utf-8
#Operadores matemáticos, comparativos e tipos de variáveis numéricas.
num = 3.14

print(type(num))

print(3 + 2) #Soma
print(3 - 2) #Subtração
print(3 * 2) #Multiplicação
print(3 / 2) #Divisão exata
print(3 // 2) #Divisão excluindo a parte decimal
print(3 ** 2) #Operação potencial
print(3 % 2) #Resto da divisão. Normalmente usado para contar par ou impar

num = 1

num += 1 #Incrementa em 1 o valor de num

num *= 10 #Multiplica por 10 o valor atual de num e salva o novo valor em num

print(num)

num = -3

print(abs(num)) #Valor absoluto (em módulo) de num

print(round(3.75, 1)) #Arredonda o valo 3.75 (primeiro argumento) com 1 (segundo argumento) casa após o ponto


#Operadores de comparação
num_1 = 3
num_2 = 2

print(num_1 < num_2) # menor que
print(num_1 > num_2) # maior que
print(num_1 <= num_2) # menor ou igual a
print(num_1 >= num_2) # maior ou igual a
print(num_1 == num_2) # igual a 
print(num_1 != num_2) # diferente de

num_1 = '100'
num_2 = '200'

print(num_1 + num_2) #print da soma de duas strings
print(int(num_1) + int(num_2)) #transforma as strings em inteiros e soma os números