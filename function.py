import os
import shutil
import config_tools


def create_dir(name_new_path):
    """This function asks the user for the path to create a working directory"""

    try:
        os.mkdir(config_tools.full_dest + name_new_path)
    except OSError:
        print("Создать директорию %s не удалось" % name_new_path)
    else:
        print("Успешно создана директория %s " % name_new_path)


def del_dir(name_del_path):
    """This function delete path"""

    try:
        os.rmdir(config_tools.full_dest+name_del_path)
    except OSError:
        print(f"Удалить директорию {name_del_path} не удалось,каталог не найден или не является пустым.")
    else:
        print(f"Директория успешно удалена {name_del_path}")


def create_file(name, text=None):
    """This function create empty file in chosen directory"""

    if os.path.exists(config_tools.full_dest+name):
        print(f"{name} уже существует, для записи текста введите его ниже, для завершения команды введите 'no': ")
        answer = input()
        if answer != "no":
            with open(config_tools.full_dest + name, 'a', encoding='utf-8') as fi:
                fi.write(answer)
                print(f"В {name} успешно записан текст")
        elif answer == "no":
            quit()
    else:
        with open(config_tools.full_dest + name, 'w', encoding='utf-8') as fi:
            print(f"{name} успешно создан")
            if text:
                fi.write(text)
                print(f"В {name} успешно записан текст")


def del_file(name_del_file):
    """This function delete path"""

    try:
        os.remove(config_tools.full_dest+name_del_file)
    except OSError:
        print(f"Удалить файл {name_del_file} не удалось, файл не найден.")
    else:
        print(f"Файл успешно удален {name_del_file}")


def get_list():
    """This function print all files and dirs"""

    print(f"Корневой каталог: {config_tools.NAME_PATH}")
    for dirpath, dirnames, filenames in os.walk(config_tools.NAME_PATH):
        # перебрать каталоги
        for dirname in dirnames:
            print("Каталог:", os.path.join(dirpath, dirname))
            # перебрать файлы
        for filename in filenames:
            print("Файл:", os.path.join(dirpath, filename))

def copy_file(name, n_name):
    """This function copy file with a new name"""

    if os.path.isfile(config_tools.full_dest+name):
        try:
            shutil.copyfile(config_tools.full_dest+name, config_tools.full_dest+n_name)
        except OSError:
            print(f"Не возможно копировать файл {name}")
        else:
            print(f"Файл {config_tools.full_dest+name} скопирован как {config_tools.full_dest+n_name}")


def move_file_in_dir(name_file, desten):
    """This function transfer file in new directory"""

    if os.path.isfile(config_tools.full_dest+name_file):
        try:
            shutil.move(config_tools.full_dest + name_file, config_tools.full_dest + desten)
        except OSError:
            print(f"Не удалось переместить {name_file} в папку:{desten}")
        else:
            print(f"Файл {name_file} находиться в папке {desten}")

def re_name(name,new_name):
    """This function rename file or directory"""

    try:
        os.rename(config_tools.full_dest+name,config_tools.full_dest+new_name)
    except OSError:
        print(f"Не удалось переименовать {name}")
    else:
        print(f"{name} успешно переименновавано в {new_name}")

def read_file(name):
    """Read a file"""
    try:
        with open(config_tools.full_dest + name, 'r', encoding='utf-8') as file:
            print(f"Файл {name}:\n" + file.read())
    except OSError:
        print(f"Не удалось открыть {name}")

def cls():
    """Clear console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def help_list(command):

    list_command = {"all_components": "Выводит список всех папок и файлов",
                    "create_dir": "Создает папку ** необходимо указывать полный путь до места создания, за исключением "
                                  "корневой директории",
                    "create_file": "Создает файл, если необходимо записать,"
                                   " текст повторите команду как для создания файла"
                                   " ** необходимо указывать полный путь до "
                                   "места создания, "
                                   "за исключением "
                                   "корневой директории",
                    "del_file": "Удаляет файл ** необходимо указывать полный путь до выбранного файла, за исключением "
                                "корневой директории",
                    "del_dir": "Удаляет папку, если в ней нет файлов ** необходимо указывать полный путь до папки, "
                               "за исключением "
                               "корневой директории",
                    "re_name": "Переименовывает папку или файл ** необходимо указывать полный путь для файла, "
                               "за исключением "
                               "корневой директории",
                    "move_file": "Перемещает файл, необходимо указывать полный путь назначения, за исключением "
                                 "корневой директории",
                    "copy_file": "Копирует файл, необходимо указывать полный путь, за исключением "
                                 "корневой директории ",
                    "cls": "Очистить консоль"
                    }
    if command == "help":
        for key, value in list_command.items():
            print("{0}: {1}".format(key, value))
    else:
        print(command+": "+list_command[command])




