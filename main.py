import task1
import task2
import task3
import task4
import task4
import task5
import task6

if __name__ == '__main__':
    while True:
        try:
            input_str = input('Введите номер задания: ')
            if len(input_str) > 2:
                if 'end' in input_str:
                    break
            else:
                task_number = int(input_str)
                match task_number:
                    case 1:
                        task1.start()
                    case 2:
                        task2.start()
                    case 3:
                        task3.start()
                    case 4:
                        task4.start()
                    case 5:
                        task5.start()
                    case 6:
                        task6.start()
                    case _:
                        raise ValueError
        except ValueError:
            print('Ошибка ввода \n')


