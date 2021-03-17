# coding=utf-8

#Usando blocos de try/except para lidar com erros.

#Linhas de código contendo erros travam o código como um todo, então é possível, ao prever uma parte que pode conter algum erro, tentar avisar para o programa que pode dar um erro para depois ele tomar outra decisão.
try: #Primeiramente o bloco dentro de try será executado, se houver sucesso, o código segue normalmente.
    f = open('tes_file.txt')
except Exception: #Se der erro ao rodar o bloco de try o código executa o comando dentro de except ao invés de travar todo o código.
    print("This files doesn't match with the directory list.")

try:
    f = open('copy_file.txt') #Nesse caso o arquivo pode ser encontrado e essa linha de código é um sucesso.
    #var = bad_bar #Aqui o código retorna um erro, visto que há uma relação entre variáveis não declaradas.
except FileNotFoundError as e: #Esse termo dentro do except especifica qual reação tomar baseada em qual tipo de erro ocorre.
    print('File still not found.')
    print(e)
except Exception as e: #Uma generalização de erros. Ou seja, qualquer erro que houver cairá dentro desse "especificação"
    print('Something is wrong.')
    print(e)
else: #Caso não existam erros o bloco dentro de else será executado. É bom usar esse bloco ao invés de colocar os comandos dentro do próprio try para evitar algum erro inesperado.
    print(f.read())
    f.close()
finally: #Esse bloco de comandos será executado existindo erros ou não.
    print('Executing the file...')


try:
    k = open('test.txt')
    if k.name == 'test.txt':
        raise Exception #Invoca manualmente o erro declarado.
except FileNotFoundError:
    print('File doesnt exists.')
except Exception:
    print('Print by raising')

