import sys
from function import create_dir, create_file, del_file, del_dir, re_name, move_file_in_dir, copy_file, \
    get_list, help_list, cls, read_file

command = sys.argv[1]

if command == "all_components":
    get_list()
elif command == "create_dir":
    name = sys.argv[2]
    create_dir(name)
elif command == "create_file":
    name = sys.argv[2]

    create_file(name)
elif command == "del_file":
    name = sys.argv[2]
    del_file(name)
elif command == "del_dir":
    name = sys.argv[2]
    del_dir(name)
elif command == "re_name":
    name = sys.argv[2]
    n_name = sys.argv[3]
    re_name(name, n_name)
elif command == "move_file":
    name = sys.argv[2]
    n_name = sys.argv[3]
    move_file_in_dir(name, n_name)
elif command == "copy_file":
    name = sys.argv[2]
    n_name = sys.argv[3]
    copy_file(name, n_name)
elif command == "read_file":
    name = sys.argv[2]
    read_file(name)
elif command == "cls":
    cls()
elif command == "help":
    name = sys.argv[2]
    help_list(name)
