import math


def mod(a, b):
    a = str(a)
    b = int(b)
    if 'n' not in a:
        if '**-1' not in a:
            return eval(a) % b
        else:
            a = int(a[:a.find('**-1')])
            if gcd(a, b) == 1:
                for i in range(0, b):
                    if (a*i -1) % b == 0:
                        return i
            else:
                return('Не существует')
    else:
        result = 0
        for n in range(-4, 10):
            new_result = eval('(' + str(a) + ') % ' + str(b))
            if n == -4:
                result = new_result
            elif new_result != result:
                return 'Решения нет \n'
        return result


def cd(number):  # canonical decomposition
    arr = []
    while number > 1:
        for i in range(2, number + 1):
            if number % i == 0:
                arr.append(i)
                number = int(number / i)
                break
    return arr


def gcd(a, b):
    a_cd = cd(a)
    b_cd = cd(b)
    cd_arr = []  # common divisors
    for divisor in a_cd:
        if divisor in b_cd:
            b_cd.remove(divisor)
            cd_arr.append(divisor)
    return math.prod(cd_arr)


def phi(number):
    cd_number = cd(number)
    phi_count = 1
    for divisor in set(cd_number):
        phi_count = phi_count * (divisor**cd_number.count(divisor) - divisor**(cd_number.count(divisor) - 1 ))
    return phi_count

def start():
    while True:
        input_str = input('Введите выражение:  ')
        work_str = input_str.lower().replace(' ', '').replace('^', '**')
        if 'mod' in work_str:
            work_str = work_str.replace('(', '').replace(')', '')
            mod_index = work_str.find('mod')
            a, b = work_str.split('mod')
            print(input_str + ' ≡ ' + str(mod(a, b)) + '\n')
        elif 'gcd' in work_str:
            a_str, b_str = work_str[4:-1].split(',')
            print(input_str + ' = ' + str(gcd(int(a_str), int(b_str))) + '\n')
        elif 'phi' in work_str:
            number = int(eval(work_str[4:-1]))
            print(input_str + ' = ' + str(phi(number)) + '\n')
        elif 'back' in work_str:
            break
        else:
            raise ValueError
