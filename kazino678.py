# КАЗИНО 678
import os
from ctypes import *

valuta = "Руб."
money = 0
defaultMoney = 10_000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xFFFFFFF5))


# Вывод сообщения о выигрыше
def pobeda(result):
    color(14)
    print(f"    Победа!!! Ваш выигрыш: {result} {valuta}")
    print(f"    У вас на счету: {money}")


# Вывод сообщения о проигрыше
def proigr(result):
    color(12)
    print(f"    Вы проиграли: {result} {valuta}")
    print(f"    У вас на счету: {money}")
    print("    Нужно отыграться!")


# Функция установки цвета текста
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)


# Функция ввода значения
def getInput(digit, message):
    color(7)
    ret = ""
    while ret == "" or not ret in digit:
        ret = input(message)
    return ret


# Функция ввода целого числа
def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while ret < minimum or ret > maximum:
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
            print("    Введи целое число!")
    return ret


# Вывод на экран цветного, обрамленного звездочками текста
def colorLine(c, s):
    os.system("cls")
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))
