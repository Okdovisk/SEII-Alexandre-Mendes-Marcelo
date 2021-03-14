# coding=utf-8
#Loops e Iterações - For/While Loops

nums = [1, 2, 3, 4, 5]

for num in nums: #Loop for simples, que faz um escaneamento utilizando a variável num sobre a lista nums.
    if num == 3:
        print('Found!')
        break #Comando de parada do loop for.
    if num == 1 or num == 2:
        continue #Comando para o código seguir normalmente.
    print(num)


for num in nums:
    for letter in 'abc': #Loop for duplo
        print(num, letter)

for i in range(0,10): #Loop for utilizando a função range, que conta a partir do valor do primeiro parametro até um anterior ao valor do segundo paramentro.
    print(i)

print('\n')

x = 0

while x < 10: #Loop while relacionado a x, ao valor do sinal da comparativo (x<10), que pode ser True ou False.
    print(x)
    x += 1 #Incrementação da variável x. Caso não a houvesse, o loop seria infinito nessas condições.

x = 0

while True: #Loop while sem condição de parada. Esse loop será infinito caso não exista algum comando de quebra (break).
    print(x)
    if x == 55:
        break #Quebra do loop.
    x += 1