from time import sleep
from sys import stdout
from random import randint
from screensavers import logo

def up():
    print(' ' * 49 + '_' *39 + ' ')
    print(' ' * 47, '|' + ' ' * 39 + '|')

def loading():
    for i in range(0, 101):
        sleep(0.035)
        print('\u001b[100D', end='')
        print(' ' * 47, '|', ' ' * 6, f'Обработка данных... {i:0>3}%', ' ' * 5, '|', end='')
        stdout.flush()
    print()

def down():
    print(' ' * 47, '|' + '_' * 39 + '|\n')

up()
loading()
down()
