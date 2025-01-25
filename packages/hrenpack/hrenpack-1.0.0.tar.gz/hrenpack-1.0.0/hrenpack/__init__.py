import os
from typing import Union, Optional
from random import randint
from hrenpack.strwork import randstr
from hrenpack.listwork import split_list

si = Union[int, str]
integer, string, boolean = int, str, bool
ColorTyping = Union[tuple[int, int, int], list[int, int, int], tuple[int, int, int, float], list[int, int, int, float]]


print("Hrenpack")
print("(c) Mag Ilyas DOMA, 2024. Distributed under a BSD license. Распостраняется с лицензией BSD.")

__version__ = '1.0'


def dec_to_hex(dec):
    d1 = dec // 16
    d2 = dec % 16

    def dth(d):
        if d == 0:
            h = '0'
        elif d == 1:
            h = '1'
        elif d == 2:
            h = '2'
        elif d == 3:
            h = '3'
        elif d == 4:
            h = '4'
        elif d == 5:
            h = '5'
        elif d == 6:
            h = '6'
        elif d == 7:
            h = '7'
        elif d == 8:
            h = '8'
        elif d == 9:
            h = '9'
        elif d == 10:
            h = 'a'
        elif d == 11:
            h = 'b'
        elif d == 12:
            h = 'c'
        elif d == 13:
            h = 'd'
        elif d == 14:
            h = 'e'
        elif d == 15:
            h = 'f'
        return h

    h1 = dth(d1)
    h2 = dth(d2)
    hex = h1 + h2
    return hex


def hex_to_dec(hex):
    def htd(h):
        if h == '0':
            d = 0
        elif h == '1':
            d = 1
        elif h == '2':
            d = 2
        elif h == '3':
            d = 3
        elif h == '4':
            d = 4
        elif h == '5':
            d = 5
        elif h == '6':
            d = 6
        elif h == '7':
            d = 7
        elif h == '8':
            d = 8
        elif h == '9':
            d = 9
        elif h == 'a':
            d = 10
        elif h == 'b':
            d = 11
        elif h == 'c':
            d = 12
        elif h == 'd':
            d = 13
        elif h == 'e':
            d = 14
        elif h == 'f':
            d = 15
        return d

    if len(hex) == 1:
        dec = htd(hex)
    elif len(hex) == 2:
        h1 = hex[0]
        h2 = hex[1]
        d1 = htd(h1)
        d2 = htd(h2)
        d16 = d1 * 16
        dec = d16 + d2
    return dec


def rgb_to_hex(red, green, blue):
    hr = dec_to_hex(red)
    hg = dec_to_hex(green)
    hb = dec_to_hex(blue)
    color = '#' + hr + hg + hb
    return color


def hex_to_rgb(hex):
    red = hex[1] + hex[2]
    green = hex[3] + hex[4]
    blue = hex[5] + hex[6]
    rgb = (red, green, blue)
    return rgb


def secondmeter():
    from time import sleep as pause

    def nplus(wh):
        if wh < 10:
            th = '0' + str(wh)
        else:
            th = str(wh)
        return th

    hours = 0
    mins = 0
    secs = 0
    msecs = 0
    while True:
        hours += 1
        for mins in range(60):
            for secs in range(60):
                for msecs in range(1000):
                    pause(0.001)
                    time = (nplus(hours) + ':' + nplus(mins) + ':' + nplus(secs) + '.' + nplus(msecs))
                    return time


def today():
    from datetime import datetime
    now = str(datetime.now()).split('-')
    td = now[-1].split()
    td.pop()
    now.pop()
    now.append(td)
    day = now[2][0]
    month = now[1]
    year = now[0]
    print(day)
    print(month)
    print(year)
    date = day + '.' + month + '.' + year
    return date


def notwork():
    print("Данная функция находится в разработке и пока не работает")


def sts(word):
    stars = '*' * len(word)
    return stars


def of_utf8(filename, mode='r'):
    file = open(filename, mode, encoding='utf-8')
    return file


def write_a(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.write(f'{str(data)}\n')
    file.close()


def write(path, text):
    file = open(path, 'w', encoding='utf-8')
    file.write(str(text))
    file.close()


# def binary_code(quantity: int, file_path: Optional[str] = None):
#     from random import randint
#     output = ''
#     for i in range(quantity):
#         ri = randint(0, 1)
#         output = '' + str(ri)
#     if file_path is None:
#         file = open(file_path, 'w')
#         file.write(output)


def null():
    pass


def switch(variable, case: dict, default=null):
    for key in case:
        func = case[key]
        if variable == key:
            func()
            break
    else:
        default()


def bincode_generator(length: int, isInt: bool = False):
    bincode = ''
    for i in range(length):
        bincode = bincode + randstr(0, 1)
    return int(bincode) if isInt else bincode


def show_help(path_of_document: str, path: str = ''):
    def return_text(pod):
        document = of_utf8(path_of_document)
        data = document.read()
        document.close()
        return data

    text = return_text(path_of_document)

    if path:
        if not os.path.isfile(path):
            raise FileExistsError(
                f'[WinError 183] Невозможно создать новый файл, так как он уже существует: {path}')
        else:
            file = of_utf8(path, 'w')
            file.write(text)
            file.close()
    else:
        print(text)


def switch_return(variable, case: dict, default=None):
    for key in case:
        value = case[key]
        if variable == value:
            output = value
            break
    else:
        output = default
    return output


def string_error(error: Exception):
    return str(error)


def who_called_me():
    import inspect
    current_frame = inspect.currentframe()
    calling_frame = current_frame.f_back
    return inspect.getfile(calling_frame)


def get_resource(path: str):
    """Вызывает ресурс hrenpack. Работает только, если вызывать внутри пакета hrenpack
    :arg path: Принимаются только пути, относительные \\hrenpack\\resources\\
    """
    python_path = who_called_me()
    python_list = python_path.split('\\')
    if 'hrenpack' not in python_list:
        raise NotADirectoryError
    hrenpack_index = python_list.index('hrenpack')
    return '\\'.join(python_list[:hrenpack_index + 1]) + '\\resources\\' + path


def one_return(count: int, value=None):
    if count == 1:
        return value
    else:
        output = list()
        for i in range(count):
            output.append(value)
        return tuple(output)


none_tuple = lambda count: one_return(count)
tuple0 = lambda count: one_return(count, 0)
str_tuple = lambda count: one_return(count, '')
