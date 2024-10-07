'''
Найдите число шагов, за которые получится единица, используя следующий процесс: берём любое натуральное число n больше
единицы. Если оно чётное, то делим его на 2, а если нечётное, то умножаем на 3 и прибавляем 1.
'''


def collatz_hypothesis(n):
    if n <= 1:
        return 'Число должно быть больше 1'
    count = 1
    num = chec(n)
    while num != 1:
        num = chec(num)
        count += 1
    return count


def chec(n):
    if n % 2 == 0:
        positive = n / 2
        return positive
    elif n % 2 != 0:
        negative = n * 3 + 1
        return negative


if __name__ == '__main__':
    print(collatz_hypothesis(3))
