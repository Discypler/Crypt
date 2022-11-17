import task1


def lcm(a, b):
    return abs(a * b) / task1.gcd(a, b)


def start():
    isu_number = int(input('Введите свой номер ИСУ: '))
    isu_number_2 = int(input('Введите номер ИСУ следующего по списку:'))
    amount = int(input('Введите количество человек в группе: '))
    b = task1.mod(isu_number_2 + 4, amount + 1)
    print(f'{isu_number_2} + 4 mod {amount} + 1 = {b}')
    print(f'НОК({isu_number}, {b}) = {int(lcm(isu_number, b))}')