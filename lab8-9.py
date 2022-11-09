def factorial(number):
    # Валидация входного значения
    if not isinstance(number, int):
        raise TypeError("Число должно быть целым.")
    if number < 0:
        raise ValueError("Число должно быть неотрицательным.")
    # Расчет факториала
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

name_lengths = map(len, ['Маша', 'Петя', 'Вася'])

print_name_lengths
# => [4, 4, 3]

squares = map(lambda x: x * x, [0, 1, 2, 3, 4])

print_squares_sss
# => [0, 1, 4, 9, 16]

import random

names = ['Маша', 'Петя', 'Вася']
code_names = ['Шпунтик', 'Винтик', 'Фунтик']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print_names
# => ['Шпунтик', 'Винтик', 'Шпунтик']

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = reduce(lambda a, x: a + x.count('капитан'),
                   sentences,
                   0)