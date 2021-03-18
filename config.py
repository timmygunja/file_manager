import os

path = None


"""Задание рабочей директории"""
def configure_path():
    global path

    print('Введите 1 для задания рабочей директории по умолчанию')
    print('Введите 2 для задания своей рабочей директории')

    while True:
        ans = input('')

        if ans == '1':
            path = os.path.join(os.getcwd(), os.environ.get("USER"))
            break
        elif ans == '2':
            path = os.path.join(os.getcwd(), input('Введите название вашей рабочей директории'))
            break

    # mypath = os.getcwd() + os.environ.get("USER")

    if os.path.isdir(os.environ.get('USER')) is False:
        os.mkdir(f'{path}')
    else:
        return f"Standard directory already exists {path}"
    return path


configure_path()
