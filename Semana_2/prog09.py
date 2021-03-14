# coding=utf-8

#Importando módulos e explorando as bibliotecas iniciais.

import my_module as mm #Importando um módulo existente num mesmo diretório e o renomeando.
#from my_module import find_index #Importando uma função específica de um módulo.
import sys
#sys.path.append('Localização/do/diretório') #Adiciona um novo caminho na busca de diretórios que contém módulos.
import random #Exemplo de módulo retirado de uma biblioteca python padrão.
import math
import datetime

courses = ['Math', 'Physics', 'Art', 'Geograph', 'History', 'CompSci']
course = 'History'

print('Where is {} between the courses?\n'.format(course))
print(mm.find_index(courses, course)) ##Chamada da função invocada

print(sys.path) #Print dos caminhos de busca para módulos importados

print(random.choice(courses)) #Exemplo de um uso do módulo random

print(math.radians(90))

print(datetime.date.today())