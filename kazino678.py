# КАЗИНО 678
import os
from ctypes import *
import time, random

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


# Анимация рулетки
def getRoulette(visible):
    tickTime = random.randint(100, 200) / 10000
    mainTime = 0
    number = random.randint(0, 38)
    increaseTickTime = random.randint(100, 110) / 100
    col = 1

    while mainTime < 0.7:
        col += 1
        if col > 15:
            col = 1

        mainTime += tickTime
        tickTime *= increaseTickTime

        color(col)
        number += 1
        if number > 38:
            number = 0
            print()

        printNumber = number
        if number == 37:
            printNumber = "00"
        elif number == 38:
            printNumber = "000"

        print(
            " Число >", printNumber, "*" * number, " " * (79 - number * 2), "*" * number
        )

        if visible:
            time.sleep(mainTime)

    return number


# Рулетка
def roulette():
    global money
    playGame = True

    while playGame and money > 0:
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}\n")
        color(11)
        print(" Ставлю на...")
        print("    1. Четное (выигрыш 1:1)")
        print("    2. Нечетное (выигрыш 1:1)")
        print("    3. Дюжина (выигрыш 3:1)")
        print("    4. Число (выигрыш 36:1)")
        print("    0. Возврат в предыдущее меню")

        x = getInput("01234", "    Твой выбор? ")

        playRoulette = True
        if x == "3":
            color(2)
            print()
            print(" Выбери числа:...")
            print("    1. От 1 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Назад")

            duzhina = getInput("0123", "   Твой выбор? ")

            if duzhina == "1":
                textDuzhina = " от 1 до 12"
            elif duzhina == "2":
                textDuzhina = " от 13 до 24"
            elif duzhina == "3":
                textDuzhina = " от 25 до 36"
            elif duzhina == "0":
                playRoulette = False
        elif x == "4":
            chislo = getIntInput(0, 36, "   На какое число ставишь? (0..36): ")

        color(7)
        if x == "0":
            return 0

        if playRoulette:
            stavka = getIntInput(
                0, money, f"    Сколько поставишь? (не более {money}): "
            )
            if stavka == 0:
                return 0

            number = getRoulette(True)
            print()
            color(11)

            if number < 37:
                print(f"    Выпало число {number}! " + "*" * number)
            else:
                if number == 37:
                    printNumber = "00"
                elif number == 38:
                    printNumber = "000"
                print(f"    Выпало число {printNumber}! ")

            # Проверяем ставки и результат
            if x == "1":
                print("    Ты ставил на ЧЁТНОЕ!")
                if number < 37 and number % 2 == 0:
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)
            elif x == "2":
                print("    Ты ставил на НЕЧЁТНОЕ!")
                if number < 37 and number % 2 != 0:
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)
            elif x == "3":
                print(f"    Ставка сделана на диапазон чисел {textDuzhina}.")
                winDuzhina = ""
                if number > 0 and number < 13:
                    winDuzhina = "1"
                elif number > 12 and number < 25:
                    winDuzhina = "2"
                elif number > 24 and number < 37:
                    winDuzhina = "3"
                if duzhina == winDuzhina:
                    money += stavka * 2
                    pobeda(stavka * 3)
                else:
                    money -= stavka
                    proigr(stavka)
            elif x == "4":
                print(f"    Ставка сделана на числo {chislo}.")
                if number == chislo:
                    money += stavka * 35
                    pobeda(stavka * 36)
                else:
                    money -= stavka
                    proigr(stavka)

            print()
            input(" Нажми Enter для продолжения...")


# Кости
def dice():
    pass


# Однорукий бандит
def oneHandBandit():
    pass


def main():
    global money, playGame

    money = loadMoney()
    startMoney = money

    while playGame and money > 0:
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

        x = getInput("1230", "    Твой выбор? ")

        if x == "0":
            playGame = False
        elif x == "1":
            roulette()
        elif x == "2":
            dice()
        elif x == "3":
            oneHandBandit()

    colorLine(12, "Жаль, что ты покидаешь нас! Но возвращайся скорей!")
    color(13)
    if money <= 0:
        print(" Упс, ты остался без денег. Возьми микрокредит и возвращайся!")

    color(11)
    if money > startMoney:
        print("Ну что ж, поздравляем с прибылью!")
        print(f"На начало игры у тебя было {startMoney} {valuta}")
        print(f"Сейчас уже {money} {valuta}! Играй ещё и приумножай!")
    elif money == startMoney:
        print(f"Твой выигрыш 0 {valuta}")
    else:
        print(f"К сожалению, ты проиграл {startMoney - money} {valuta}")
        print("В следующий раз всё обязательно получится!")

    saveMoney(money)

    color(7)
    quit(0)


main()
