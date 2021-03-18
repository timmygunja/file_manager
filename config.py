import os

path = None


def configure_path():
    global path
    path = os.path.join(os.getcwd(), os.environ.get("USER"))
    # mypath = os.getcwd() + os.environ.get("USER")

    if os.path.isdir(os.environ.get('USER')) is False:
        os.mkdir(f'{path}')
    else:
        return f"Standard directory already exists {path}"
    return path


configure_path()
