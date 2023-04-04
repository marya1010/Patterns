from functions import *
import os
import re


#path C:\Users\hrenz\Documents\GitHub\Patterns\Files_test

def get_path():
    print('Введите путь к необходимой папке. Его нельзя будет поменять.')
    path = input()
    return path


def match(text):
    pattern = '[A-Z]+'
    if re.search(pattern, text):
        return re.search(pattern, text).group(0)
    else:
        return 'Прочее'


path = get_path()
create_folder(path, name='Прочее') # создается папка Прочее
files = os.listdir(path)
for file in files:
    folder = match(file)
    create_folder(path, folder)
    move_file(path, file, folder)
print('Файлы распределены!')
