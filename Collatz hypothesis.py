'''
Найдите число шагов, за которые получится единица, используя следующий процесс: берём любое натуральное число n больше
единицы. Если оно чётное, то делим его на 2, а если нечётное, то умножаем на 3 и прибавляем 1.
'''


def collatz_hypothesis(n):
    if n <= 1:
        return 'Число должно быть больше 1'

    return chec(n)


def chec(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = (n * 3 + 1) / 2
            count += 2
    return count


if __name__ == '__main__':
    print(collatz_hypothesis(6))
