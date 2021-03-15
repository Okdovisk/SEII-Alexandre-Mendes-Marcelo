# coding=utf-8

import csv #Módulo específico para lidar com esse tipo de arquivo.

with open('e-mails.csv', 'r') as csv_file: #Uma abertura idêntica à de arquivos de texto.
    csv_reader = csv.reader(csv_file) #Esse método de leitura coloca em csv_reader listas nas quais cada linha é uma lista com cujos elementos são os dados separados pelas vírgulas.
    for line in csv_reader:
        print(line) #Print das linhas. É possível fazer o print dos elementos da lista, basta passar o parâmetro index list[index].
        next(csv_reader) #Método que pula uma lista (linha) existente em csv_reader.

with open('e-mails.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_e-mails.csv', 'w') as new_file: #Cria ou abre o arquivo new_e-mail.csv no modo escrita.
        csv_writer = csv.writer(new_file, delimiter='\t') #Insere no escritor o nome do arquivo no qual será escrito e o tipo de caracter que irá separar os elementos.

        for line in csv_reader:
            csv_writer.writerow(line)

with open('new_e-mails.csv', 'r') as new_csv_file: #Abrindo o arquivo criado no modo leitura.
    csv_reader = csv.reader(new_csv_file, delimiter='\t') #É preciso definir o delimitador caso o arquivo csv não esteja com seus elementos separados por vírgulas.

    for line in csv_reader:
        print(line)

with open('new_e-mails.csv', 'r') as dic_mod:
    csv_reader = csv.DictReader(dic_mod, delimiter='\t') #Lê e armazena as linhas e elementos em modo dicionário, organizando os dados baseado na especificação da primeira linha.

    for line in csv_reader: #Pegando apenas os e-mails da lista de dados existentes no arquivo csv.
        print(line['E-mail']) #Uma forma muito mais intuitiva de escrever o código.

with open('e-mails.csv', 'r') as csv_reader:
    csv_reader = csv.DictReader(csv_reader)
    with open('another_e-mails.csv', 'w') as another: #Escrita de arquivo csv na forma de dicionário.
        fieldnames = ['Name', 'Last_Name'] #Seleção dos elementos para serem escritos.
        csv_writer = csv.DictWriter(another, fieldnames=fieldnames)

        csv_writer.writeheader() #Função para imprimir também o cabeçalho inicial.

        for line in csv_reader:
            del line['E-mail'] #Deletando a chave 'E-mail' e o valo relacionado a ela.
            csv_writer.writerow(line)