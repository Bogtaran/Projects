"""Программа находит простые числа до тех пор, пока пользователь не перестанет спрашивать."""


def main():
    per = 'д'
    my_iter_prime = iter(list_prime())
    print('Приветствую вас! Вы хотите узнать простые числа по порядку?')
    per = input('Введите "д" - для продолжения, или "н" - что бы закончить: ')
    print()
    while per.lower() == 'д':
        try:
            print(next(my_iter_prime))
            per = input('Желаете узнать следующее простое число: ')
        except StopIteration:
            print()
            print('Числа закончились.')
            per = input('Желаете начать сначала?: ')
            print()
            if per.lower() == 'д':
                my_iter_prime = iter(list_prime())
                print(next(my_iter_prime))
                per = input('Желаете узнать следующее простое число: ')
    print()
    print('До свидания')


def is_prime(A):
    """Данная функция проверяет: является ли число простым"""
    if A == 1 or A == 2 or A == 3:
        return True
    for i in range(2, A):
        if i == A - 1:
            return True
        elif A % i != 0:
            i += 1
        else:
            return False


def list_prime():
    """Данная функция создает список с простыми числами по порядку. Можно указать диапазон, к котором будут выдаваться
    простые числа."""
    list_primes = []
    for j in range(1, 10000):  # диапазон, в котором будут выдаваться простые числа
        if is_prime(j):
            list_primes.append(j)
    return list_primes


if __name__ == '__main__':
    main()
