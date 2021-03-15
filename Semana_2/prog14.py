# coding=utf-8

#Análise e renomeação de múltiplos arquivos.

import os
path_random = os.getcwd() + '/Names/Random'
path_organized = os.getcwd() + '/Names/Organized'

for f in os.listdir(path_random):
    f_name, f_ext = os.path.splitext(f)
    f_title, f_number = f_name.split('-')
    f_number = f_number.zfill(2)

    new_name = '{}-{}{}'.format(f_number, f_title, f_ext)
    print(new_name)

    os.chdir(path_organized)
    with open('{}'.format(new_name), 'w'):
        pass
