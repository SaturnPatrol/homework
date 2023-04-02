import random

balance = 10000
kubik = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
bet_log = []
while (balance > 999):
        predict = int(input('Угадай число..? '))
        result = random.choice(kubik)
        if predict == result:
            balance += 1000
            print('Игра загадала: ' + str(result) + ', моя попытка: ' + str(predict) + ', на счету: ' + str(balance))
            bet_log.append('Игра загадала: ' + str(result) + ', моя попытка: ' + str(predict) + ', на счету: ' + str(balance))
        elif (predict < 2 or predict > 12):
            print('некорректный кубик')
        else:
            balance -= 1000
            print('Игра загадала: ' + str(result) + ', моя попытка: ' + str(predict) + ', на счету: ' + str(balance))
            bet_log.append('Игра загадала: ' + str(result) + ', моя попытка: ' + str(predict) + ', на счету: ' + str(balance))

#Выводим журнал ставок построчно:
print('---------------------------')
print('Журнал ставок:')
for i in bet_log:
    print(i)

