# coding=utf-8

#Manipulando arquivos
#Leitura

f = open('test.txt', 'r') #Abrindo o arquivo especificado no modo leitura.
print(f.name) #Print do dado nome
print(f.mode + '\n') #Print do dado modo de manipulação
f.close() #É preciso fechar manualmente o arquivo para evitar erros e/ou alterações indesejadas.

with open('test.txt', 'r') as f: #Usar esse modo de abrir arquivos é uma boa prática, por todas as manipulações ficam dentro do bloco e o arquivo é fechado automaticamente.
    print(f.read()) #Simplesmente exibe o conteúdo do arquivo.
    #f.readlines() #Divide o arquivo por meio das linhas e as salva em ordem numa lista.
print(f.closed) #Prova de que o arquivo foi realmente fechado.
print(f.name + '\n') #Apesar de ter fechado o arquivo, as informações sobre ele foram armazenadas previamente.

with open('test.txt', 'r') as f:
    for line in f: #Lê linha por linha, indo para a próxima sempre que a função é chamada novamente.
        print(line)

with open('test.txt', 'r') as f:    
    print(f.read(10)) #Mostrando que é possível ler um número específico de caracteres.
    print(f.read(20)) #Mostrando que a leitura retorna onde antes ela parou.
    print(f.tell()) #Diz onde em qual posição de caracter a leitura parou.
    f.seek(0) #Coloca a leitura do arquivo na posição especificada por parâmetro.
    print(f.tell())

#Escrita

with open('text_2.txt', 'w') as f: #Cria um arquivo e abre no modo escrita.
    f.write('Test.') #Escreve no arquivo criado.
    f.seek(0) #Seek também pode ser usado para apontar para uma posição específica a ser escrita.
    f.write('Test.')
    f.seek(0)
    f.write('R') #Caso já existe algum caracter na posição a ser escrita, a escrita apenas substitui o caracter.

with open('test.txt', 'r') as rf:
    with open('copy_file.txt', 'w') as wf:
        for line in rf:
            wf.write(line) #Copia por inteiro o conteúdo de um arquivo aberto no modo leitura para um arquivo no modo escrita.

#with open('lena.jpg', 'rb') as rf:
#    with open('lena_copy.jpg', 'wb') as wf:
#        for line in rf:
#            wf.write(rf) #Também faz uma cópia completa do arquivo, porém no modo binário, visto que esse é o formato para imagens. Para diferenciar assim, basta acrescentar o 'b' (binary) juntamente ao modo de manipulação.