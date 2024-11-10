'''
Функция принимает 2 списка. Первый - это баллы, полученные студентами, второй - фамилии студентов. Длина списков равна.
Необходимо вывести фамилии студентов, набравших 35 баллов или более. Если никто из студентов не набрал нужное количество
баллов, то вывести 'Никто'.
'''

def filter_passed_students(score_string: str, name_string: str) -> list[str]:
    score_string = score_string.split(',')
    name_string = name_string.split(',')
    c = [name_string[i] for i in range(len(score_string)) if int(score_string[i]) >= 35]
    if len(c) == 0:
        c.append('Никто')
    return c


if __name__ == '__main__':
    passed_students = filter_passed_students('1,35,4,5,36,7,8,9,10,14', 'Ola,Kir,Tatiana,Ramin,'
                                                                      'Valentin,Rick,Polya,Margarita,Ilya,Fiona')
    for student in passed_students:
        print(student)

