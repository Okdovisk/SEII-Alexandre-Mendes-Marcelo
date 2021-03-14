# coding=utf-8

#Funções
#Sem parâmetros.

def hello_function_print(): #Função que faz um print ao ser chamada.
    print('Hello, function! Print mod')

def hello_function_return(): #Função que retorna uma string
    return 'Hello, function! Return mod.'

hello_function_print() #Chamada da função hello_function_print.

print(hello_function_return().upper()) #Chamada da função hello_function_return. Podemos tratar a chamada da função diretamente como uma string.

#Com parâmetros

def hello_greeting(greeting, name='you'): #Função de retorno com parâmetros. O parâmetro name está declarado como padrão, ou seja, será utilizado o nome em questão caso outro não seja passado como parâmetro.
    return '{}, {}!'.format(greeting, name)

print(hello_greeting('Hi'))

def student_info(*args, **kwargs): #Função especial que utiliza dados de posição e valores chaveados arbitrários. Os nomes args e kwargs são convencionais.
    print(args) #args são tupples/listas de posições sem quantidade prévia definida.
    print(kwargs) #kwargs são dicionários sem quantidade de chaves/valores definidos.

lst = ['Math', 'Art']
Dict = {'name':'John', 'age':22}

student_info('Math', 'Art', name='John', age=22)
#student_info(*lst, **Dict) #Para passar os valores por meio de listas/tupples/dicionários prontos é preciso usar as devidas *'s para especificar as informações.

