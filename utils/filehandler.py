import os


def exist(filename) -> bool:
    return os.path.exists(f'./repo/{filename}')


def read_content(filename) -> str:
    path = f'./repo/{filename}'
    with open(path) as f:
        contents = f.read()
        f.__setattr__('desc', 'test file')
        print('DESCRIPTION: ', f.__getattribute__('desc'))
        return contents


def read_desc(filename) -> str:
    path = f'./repo/{filename}'
    with open(path) as f:
        desc = f.__getattribute__('desc')
        return desc
