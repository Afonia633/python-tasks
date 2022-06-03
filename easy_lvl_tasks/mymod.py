"""Основы импортирования. Напишите программу, которая подсчитывает ко-
личество строк и символов в файле (в духе утилиты wc в операционной систе-
мы UNIX). В своем текстовом редакторе создайте модуль с именем mymod.
py, который экспортирует три имени:
• Функцию countLines(name), которая читает входной файл и подсчитывает
число строк в нем (подсказка: большую часть работы можно выполнить
с помощью метода file.readlines, а оставшуюся часть – с помощью функ-
ции len).
• Функцию countChars(name), которая читает входной файл и подсчитыва-
ет число символов в нем (подсказка: метод file.read возвращает единую
строку).
• Функцию test(name), которая вызывает две предыдущие функции с за-
данным именем файла. Вообще говоря, имя файла можно жестко
определить в программном коде, принимать ввод от пользователя или
принимать имя как параметр командной строки через список sys.argv –
но пока исходите из предположения, что оно передается как аргумент
функции."""
def countLines(name):
    file1 = open(name, 'r')
    lines = 0
    while True:
        line = file1.readline()
        if not line:
            break
        lines += 1
    print('Total lines: ', lines)
    file1.close()


def countChars(name):
    file1 = open(name, 'r')
    chars = len(file1.read())
    print('Total chars: ', chars)
    file1.close()


def test(name):
    file_1 = str(name)
    countLines(file_1)
    countChars(file_1)
