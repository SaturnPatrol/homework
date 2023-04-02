zarplata1 = int(input('Укажите зарплату первого человека? '))
zarplata2 = int(input('Укажите зарплату второго человека? '))
zarplata3 = int(input('Укажите зарплату третьего человека? '))

trata = (zarplata1 + zarplata2 + zarplata3) // 90
print('Вы можете тратить по ' + str(trata) + ' рублей в день')