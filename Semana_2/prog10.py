# coding=utf-8

#Módulo os

import os #Módulo específico para manipular as entrelinhas do sistema operacional.
from datetime import datetime

print(os.getcwd()) #Print do caminho para o diretório atual.

#os.chdir('/Outro/caminho/de/diretório') #Muda do diretório atual para outro diretório.

print(os.listdir(os.getcwd())) #Lista os arquivos e diretórios existentes dentro do diretório em parâmetro.

os.makedirs('creat_dir/sub_creat_dir/') #Cria um diretório e um subdiretório como especificado no parâmetro.
os.removedirs('creat_dir/sub_creat_dir/') #Remove o diretório e o sub diretório criado.
# os.rename('file.py', 'new_file.py') #Renomeia o arquivo citado.
print(os.stat('prog09.py')) #Print de alguns dados relacionados ao arquivo.

print(datetime.fromtimestamp(os.stat('prog09.py').st_mtime)) #Print da data de modificação do arquivo prog09.py com filtro de dados do datetime

for caminho_dir, nomes_dirs, arquivos_dir in os.walk('Caminho/de/um/diretório'): #Percorre listando todos os nomes dos diretórios e arquivos existentes no caminho passado.
    continue

recipe_file = os.path.join(os.environ.get('HOME'), 'text.txt') #Cria uma receita para a criação de um arquivo a partir de uma junção dos dois parâmetros dentro de join.
print(recipe_file)

print(os.path.basename('/temp/test.txt')) #Print do nome base (ultimo nome especificado) do caminho indicado.
print(os.path.dirname('/temp/test.txt')) #Print do diretório especificado
print(os.path.split('/temp/test.txt')) #Print separado dos diretórios e arquivos inseridos.
print(os.path.exists('/tmp/test.txt')) #Print que verifica se o caminho passado realmente existe.
print(os.path.isdir('/tmp/test.txt')) #Print que verifica se o caminho passa um diretório.
print(os.path.isfile('/tmp/test.txt')) #Print que verifica se o caminho é de um arquivo.
print(os.path.splitext('/tmp/test.txt')) #Print que separa o caminho descrito entre antes e depois do ponto. Útil para separar os nomes dos tipos de arquivo.
