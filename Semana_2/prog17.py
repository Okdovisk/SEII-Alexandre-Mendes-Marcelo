# coding=utf-8

#Módulo datetime. Como trabalhar com datas, tempos, diferenças de tempos e zonas temporais.

import datetime

today = datetime.date.today() #Função para salvar a data do dia atual.

print(today)
print(today.weekday()) #Print do dia da semana em inteiro de zero a seis (segunda = 0, doming = 6).
print(today.isoweekday()) #Print do dia da semana em inteiro de um a sete (segunda = 1, domingo = 7).

t_delta = datetime.timedelta(days=7) #Cria uma variável temporal de dimensão e quantidade definidas pela parâmetro.
print(today + t_delta) #Print de uma data resultante da soma do dia atual com uma semana.

christmas = datetime.date(2021, 12, 25) #Salva uma data específica em uma variável.
until = christmas - today

print(until) #Print em dias de quanto falta até chegar a data especificada.

dt = datetime.datetime(2020, 4, 11, 15, 30, 30, 100000) #Preenchendo a variável dt com os valores de data e horário especificados.

print(dt.date()) #Acessando apenas a data da variável de tempo criada.
print(dt.time()) #Acessando apenas o horário da variável de tempo criada.

dt_today = datetime.datetime.today() #Guarda na variável a informação da data completa da zona temporal atual
dt_now = datetime.datetime.now() #Guarda na variável a informação da data completa da zona especificada dentro dos parênteses. Caso não tenha nada especificado, fica sendo a zona atual.
dt_utc = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utc)