import os
import shutil


# функция создания папки
def create_folder(path, name):
    try:
        os.mkdir(str(path + '\\' + name))
    except FileExistsError:
        print('Папка с таким названием уже существует!')


# Удаление файла или папки
def delete_file(path, name=None):
    if name == None:
        print("Введите название файла или папки, которую нужно удалить.")
        name = input()
    if os.path.isdir(str(path + '\\' + name)):
        os.rmdir(str(path + '\\' + name))  # delete folder
    else:
        os.remove(str(path + '\\' + name))  # delete file


# Просмотр списка файлов и папок
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Перемещение файлов
def move_file(path, file, folder):
    path_moving = str(path + '\\' + file)
    shutil.copy(path_moving, path + '\\' + folder)
    delete_file(path, file)
