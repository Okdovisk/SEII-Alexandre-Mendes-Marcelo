# coding=utf-8
#Dicionários

#Armazenam chaves e valores que são interligados entre si por meio de : e chaves separadas por ,
#O dicionário relaciona todos os tipos de variáveis

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']} #Criação de um dicionário

print(student) #Print do dicionário inteiro
print(student['name']) #Print do valor relacionado à chave name
print(student.get('phone', 'Not found')) #Print do valor relacionado à chave phone. CASO essa chave não exista no dicionário o valor retornado será Null (ou o que for especificado no segundo argumento) e não dará erro no restante do código

student.update({'name': 'Jane', 'age': 26, 'phone': '555-555'}) #Atualiza o dicionário sobrescrevendo os novos valores relacionados às chaves já existentes ou criando novas chaves com valores, caso não existam ainda

print(student)

del student['age'] #Remove a chave e o valor do dicionário
courses = student.pop('courses') #Remove a chave courses juntamente com seus valores mas os salva na variável nova

print(len(student)) #print da quantidade de chaves existentes no dicionário
print(student.keys()) #print somente das chaves no dicionário
print(student.values()) #print somente dos valores no dicionário
print(student.items()) #print dos pares (chave-valor) do dicionário

for key, value in student.items(): #Outra forma de acessar as chaves e valores do dicionário
    print(key, value)