import os
from config import path
from shutil import copyfile, move, rmtree

mypath = path
head_dir = os.path.split(mypath)[1]


class Manager:
    """Получение текущего абсолютного пути"""
    def pwd(self):
        return mypath

    """Перемещение вверх из текущей папки"""
    def move_up(self):
        global mypath
        if os.path.split(mypath)[1] != head_dir:
            mypath = os.path.split(mypath)[0]
            return mypath
        else:
            return "Cannot go up"

    """Создание файла"""
    def create_file(self, name):
        file_name = os.path.join(mypath, name)
        if os.path.isfile(fr'{os.path.join(mypath, name)}') is False:
            file = open(fr'{file_name}', 'w')
            file.close()
            return f'{file_name} created'
        else:
            return f'File {name} already exists'

    """Запись содержимого в файл"""
    def write_file(self, name, text):
        with open(os.path.join(mypath, name), 'w') as f:
            f.write(text)
            return f'Written some text to file {name}'

    """Чтение файла"""
    def read_file(self, name):
        file = os.path.isfile(os.path.join(mypath, name))
        if file:
            with open(os.path.join(mypath, name), 'r') as f:
                read = f.read()
            return read
        else:
            return f"File {name} does not exist"

    """Удаление файла"""
    def delete_file(self, name):
        file = os.path.isfile(os.path.join(mypath, name))
        if file:
            os.remove(os.path.join(mypath, name))
            return f'File {name} deleted'

    """Копирование файла"""
    def copy_file(self, name, to):
        directory = os.path.isdir(os.path.join(mypath, os.path.split(to)[0]))
        file = os.path.isfile(os.path.join(mypath, name))
        if file and directory:
            copyfile(os.path.join(mypath, name), os.path.join(mypath, to))
            return f"File {os.path.join(mypath, name)} copied to {os.path.join(mypath, to)}"
        elif file is False:
            return f"File {name} not found"
        else:
            return f"Directory {to} not found"

    """Перемещение файла"""
    def move(self, name, to):
        directory = os.path.isdir(os.path.join(mypath, os.path.split(to)[0]))
        file = os.path.isfile(os.path.join(mypath, name))
        if file and directory:
            move(os.path.join(mypath, name), os.path.join(mypath, to))
            return f"File {name} was moved to {to}"
        elif file is False:
            return f"File {name} not found"
        else:
            return f"Directory {os.path.join(mypath, to)} not found"

    """Переименование файла"""
    def rename(self, name, newname):
        file = os.path.isfile(os.path.join(mypath, name))
        if file:
            os.rename(os.path.join(mypath, name), os.path.join(mypath, newname))
            return f"File {name} renamed to {newname}"

    """Создание директории"""
    def mk_dir(self, name):
        if os.path.isdir(fr'{os.path.join(mypath, name)}') is False:
            os.mkdir(f"{os.path.join(mypath, name)}")
            directory = os.path.join(mypath, name)
            return f'Directory {directory} created'
        else:
            return f'Папка уже создана'

    """Удаление директории"""
    def rm_dir(self, name):
        if os.path.isdir(f'{os.path.join(mypath, name)}'):
            rmtree(f"{os.path.join(mypath, name)}")
        else:
            return 'Directory doesn\'t exist'

        return f"Deleted directory {name}"

    """Перемещение по указаному пути"""
    def move_to_path(self, name):
        global mypath
        if os.path.isdir(f'{os.path.join(mypath, name)}'):
            mypath = fr'{os.path.join(mypath, name)}'
            return mypath
        else:
            return 'Directory doesn\'t exist'


if __name__ == '__main__':
    file_manager = Manager()
    from config import path
    print('File manager started')

    while True:
        user_input = input('').split(' ')

        try:
            if user_input[0] == 'quit':
                print('File manager finished')
                break
            elif user_input[0] == 'pwd':
                print(file_manager.pwd())
                continue
            elif (user_input[0]) == 'cdup':
                print(file_manager.move_up())
            elif (user_input[0]) == 'mkdir':
                print(file_manager.mk_dir(user_input[1]))
            elif (user_input[0]) == 'rmdir':
                print(file_manager.rm_dir(user_input[1]))
            elif (user_input[0]) == 'cd':
                print(file_manager.move_to_path(user_input[1]))
            elif (user_input[0]) == 'mkfile':
                print(file_manager.create_file(user_input[1]))
            elif (user_input[0]) == 'readfile':
                print(file_manager.read_file(user_input[1]))
            elif (user_input[0]) == 'rmfile':
                print(file_manager.delete_file(user_input[1]))
            elif (user_input[0]) == 'cpfile':
                print(file_manager.copy_file(user_input[1], user_input[2]))
            elif (user_input[0]) == 'mvfile':
                print(file_manager.move(user_input[1], user_input[2]))
            elif (user_input[0]) == 'renamefile':
                print(file_manager.rename(user_input[1], user_input[2]))
            elif (user_input[0]) == 'writefile':
                print(file_manager.write_file(user_input[1], text=str(" ".join(i for i in user_input[2:]))))
            else:
                print("Command not found")
        except IndexError:
            print("Invalid number of arguments given")
