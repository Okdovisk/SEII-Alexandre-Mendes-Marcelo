# coding=utf-8
#!/usr/bin/python3

import time
import requests
import concurrent.futures

img_urls = [
    'https://unsplash.com/photos/m3hn2Kn5Bns',
    'https://unsplash.com/photos/Mf23RF8xArY',
    'https://unsplash.com/photos/13W6AqIKV_I',
    'https://unsplash.com/photos/uIemlFWQSC4',
    'https://unsplash.com/photos/jFAG_ixCrsM',
    'https://unsplash.com/photos/_KaMTEmJnxY',
    'https://unsplash.com/photos/_vMqdG9yjqs',
    'https://unsplash.com/photos/i4XLJmlYit4',
    'https://unsplash.com/photos/ExxuYNsViC4',
    'https://unsplash.com/photos/dStdT8FxiF8',
    'https://unsplash.com/photos/NcH5I25xuX4',
    'https://unsplash.com/photos/e8uB23q9yl8',
    'https://unsplash.com/photos/dBmScckh7y0',
    'https://unsplash.com/photos/_Pi7lLcPZfM'
] #14 url's de imagens do site de mostrado no vídeo.

start_download = time.perf_counter() #Inicia a contagem de tempo.

def downloadImages(img_urls): #Cria uma função que será usada nas threads para fazer todo o processo de download das imagens.
    img_bytes = requests.get(img_urls).content #Extrai, por meio do requests.get, o conteúdo em bytes existente nos url's.
    img_name = img_urls.split('/')[4] #Separa a url pelas barras, usando o conteúdo após a 4ª para nomear a imagem.
    img_name = '{}.jpeg'.format(img_name) #Adiciona a extensão .jpeg ao nome da imagem.

    with open(img_name, 'wb') as img_file: #Cria um arquivo no modo escrita em binário para fazer a cópia local de modo compatível aos dados extraídos das url's das imagens.
        img_file.write(img_bytes) #Escreve dentro do novo arquivo o conteúdo extraído pelo requests.get.Ou seja, a imagem.
        print('{} was downloaded.'.format(img_name)) #Avisa que o download foi concluído.

with concurrent.futures.ThreadPoolExecutor() as executor: #Organiza as inicializações das threads dentro de um conjunto executor que só é concluído quando todas as threads dão alguma resposta.
    executor.map(downloadImages, img_urls) #Inicia as threads (função que faz o download das imagens) e exibe seus resultados na ordem em que foram iniciadas.

end_download = time.perf_counter() #Finaliza a contagem de tempo.

print('End all the downloads in {} seconds'.format(round(end_download - start_download, 4))) #Exibe o tempo gasto para executar o código.