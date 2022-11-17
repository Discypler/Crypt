import task1

def start():
    while True:
        isu_number = int(input('Введите номер ИСУ: '))
        cd_arr = task1.cd(isu_number)
        cd_str = ''.join(' * ' + str(num)  for num in cd_arr)
        print('Каноническое разложение^: ' + str(isu_number) + ' = 1' + cd_str)
