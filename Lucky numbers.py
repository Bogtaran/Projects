'''
Счастливое число определено следующим процессом. Начиная с некоторого положительного целого числа, замените число
суммой квадратов его цифр и повторяйте процесс до тех пор, пока число не будет равным одному(на чем все и остановится)
или оно будет циклиться бесконечно. Если цикл конечен, то изначальное число называется счастливым.
Найдите первые 8 счастливых чисел.
'''


def main():
    lucky_num = []
    count = 0
    for i in range(10, 1000):
        if lucky_number(i, lucky_num):
            lucky_num.append(i)
            count += 1
            if count == 8:
                return print(lucky_num)


def sum_squares_digits(i):
    """Данная функция находит сумму квадратов цифр числа"""
    i = str(i)
    numbers = sum([int(j) ** 2 for j in i])
    if numbers in [2, 3, 4, 5, 6, 7, 8, 9]:
        return 0
    return numbers


def lucky_number(i, lucky_num):
    """Данная функция выясняет счастливое число или нет"""
    num = sum_squares_digits(i)
    if num == 1 or num in lucky_num:
        return True
    elif num == 0:
        return False
    else:
        try:
            lucky_number(num, lucky_num)
        except RecursionError:
            return False


if __name__ == '__main__':
    main()
