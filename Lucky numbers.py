def main():
    lucky_numbers = []
    for i in range(10, 20):
        num = sum_squares_digits(i)
        if num == 1 or num == 10 or num == 13:
            lucky_numbers.append(i)
        elif len(str(num)) >= 2:
            sum_squares_digits(num)
    return lucky_numbers


def sum_squares_digits(i):
    """Данная функция находит сумму квадратов цифр числа"""
    i = str(i)
    numbers = sum([int(j) ** 2 for j in i])
    return numbers


if __name__ == '__main__':
    main()
