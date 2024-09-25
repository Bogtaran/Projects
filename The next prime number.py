"""Программа находит простые числа до тех пор, пока пользователь не перестанет спрашивать."""


def main():
    pass


def is_prime(A):  # является простым
    if A == 1 or A == 2 or A == 3:
        return True
    for i in range(2, A):
        while A % i != 0:
            i += 1
            if i == A - 1:
                return True
        return False


def list_prime():
    list_primes = []
    for j in range(1, 1000):
        is_prime(j)
        if is_prime(j):
            list_primes.append(j)
    return list_primes


if __name__ == '__main__':
    print(list_prime())
