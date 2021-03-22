import os
import shutil

# определяем текущий каталог и печатаем




def create_work_dir():
    """This function asks the user for the path to create a working directory"""
    global PATH
    name_new_path = input("Введите полный путь до места создания"
                          "директории: ")
    PATH = name_new_path

    try:
        os.mkdir(name_new_path)
    except OSError:
        print("Создать директорию %s не удалось" % name_new_path)
    else:
        print("Успешно создана директория %s " % name_new_path)





def del_work_dir():
    """This function delete path"""

    name_del_path = input("Введите название папки, которую вы хотите удалить: ")
    # check if folder exists
    try:
        if os.path.exists(name_del_path):
            # remove if exists
            shutil.rmtree(name_del_path)
    except OSError:
        print("Удалить директорию %s не удалось" % name_del_path)
    else:
        print(f"Директория успешно удалена {name_del_path}")





def create_empty_file():
    """This function create empty file in chosen directory"""

    print(PATH)
    name_new_file = input("ВВедите название файла: ")
    name_directory = input("В какую папку вы хотите сохранить файл: ")



