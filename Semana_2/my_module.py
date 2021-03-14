# coding=utf-8
#Módulo para a criação do prog09.py
print('Module in.')
def find_index(to_search, target):
    """Find the index file within a to_search location"""
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1