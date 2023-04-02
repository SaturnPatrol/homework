import random

balance = 10000
kubik = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
while (balance > 999):
        predict = int(input('Угадай число..? '))
        result = random.choice(kubik)
        if predict == result:
            balance += 1000
            print('Твоё значение ' + str(predict))
            print('На кубиках ' + str(result))
            print('Повезло, твой баланс = ' + str(balance))
        elif (predict < 2 or predict > 12):
            print('некорректный кубик')
            break
        else:
            balance -= 1000
            print('Твоё значение ' + str(predict))
            print('На кубиках ' + str(result))
            print('Не повезло, твой баланс = ' + str(balance))

