# coding=utf-8
#!/usr/bin/python3

import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'm3hn2Kn5Bns.jpeg',
    'Mf23RF8xArY.jpeg',
    '13W6AqIKV_I.jpeg',
    'uIemlFWQSC4.jpeg',
    'jFAG_ixCrsM.jpeg',
    '_KaMTEmJnxY.jpeg',
    '_vMqdG9yjqs.jpeg',
    'i4XLJmlYit4.jpeg',
    'ExxuYNsViC4.jpeg',
    'dStdT8FxiF8.jpeg',
    'NcH5I25xuX4.jpeg',
    'e8uB23q9yl8.jpeg',
    'dBmScckh7y0.jpeg',
    '_Pi7lLcPZfM.jpeg'
] #Nome das 14 imagens anteriormente baixadas e que passarão por um filtro Gausiano em modo multiprocessamento.

start_download = time.perf_counter() #Inicia a contagem de tempo.

size = (1200, 1200) #Tamanho em pixel das novas fotos. Ou seja, elas serão redimensionadas.

def processImages(img_names): #Função que recebe a lista dos nomes das imagens e faz o processamento das imagens.
    img = Image.open(img_names) #Abre a imagem usando o Pillow para trabalhar com os dados.
    img = img.filter(ImageFilter.GaussianBlur(15)) #Aplica um filtro de "borrão" Gaussiano na imagem.

    img.thumbnail(size) #Cria a miniatura da imagem com o filtro aplicado.
    img.save('processed/{}'.format(img_names)) #Salva a imagem no diretório processed/ com seu respectivo nome.
    print('{} was processed.'.format(img_names)) #Avisa que a imagem foi processada.

with concurrent.futures.ProcessPoolExecutor() as executor: #Organiza as inicializações dos processos dentro de um conjunto executor que só é concluído quando todos os processos dão alguma resposta.
    executor.map(processImages, img_names) #Inicia os processos nos cores do computador e exibe seus resultados na ordem em que foram iniciadas.

end_download = time.perf_counter() #Finaliza a contagem de tempo.

print('End all the downloads in {} seconds'.format(round(end_download - start_download, 4))) #Exibe o tempo gasto para executar o código.