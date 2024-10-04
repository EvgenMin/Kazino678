# КАЗИНО 678
import os
from ctypes import *

valuta = "Руб."
money = 0
defaultMoney = 10_000
playGame = True
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


# Чтение из файла оставшейся суммы
def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m


# Запись суммы в файл
def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла, наше Казино закрывается!")
        quit(0)


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


def main():
    global money, playGame

    money = loadMoney()
    startMoney = money

    while (playGame and money>0):
        colorLine(10, "Приветствую тебя в нашем казино, дружище!")
        color(14)
        print(f"У тебя на счету {money} {valuta}")

        color(6)
        print("Ты можешь сыграть в:")
        print("    1. Рулетку")
        print("    2. Кости")
        print("    3. Однорукого бандита")
        print("    0. Выход. Ставка 0 в играх - Выход.")
        color(7)

        x = getInput("1230","    Твой выбор?")

        if (x == "0"):
            playGame = False
        elif(x == "1"):
            # roulette()
            pass 
        elif(x == "1"):
            # dice()
            pass 
        elif(x == "1"):
            # oneHandBandit()
            pass 


        