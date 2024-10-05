'''
Найдите число шагов, за которые получится единица, используя следующий процесс: берём любое натуральное число n больше
единицы. Если оно чётное, то делим его на 2, а если нечётное, то умножаем на 3 и прибавляем 1.
'''


def collatz_hypothesis(n):
    count = 0
    if n <= 1:
        return 'Число должно быть больше 1'
    elif n%2 == 0:
        a = positive(n)
        count +=1
    elif n%2 != 0:
        a = negative(n)
        count +=1



def positive(n):
    return n / 2


def negative(n):
    return n * 3 + 1


if __name__ == '__main__':
    main()
