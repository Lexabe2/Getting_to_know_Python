# Задание 1.(БАЗОВЫЕ)

name = input("Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
citi = input("А в каком городе ты живешь? ")
citi_population = input("Сколько людей в твоем городе? ")
print(f'Тебя зовут {name}, очень приятно познакомиться, {age} какой ты большой. \n{citi} я слышал про этот город, говорят он очень красивый и в нем живет много людей аж {citi_population} человек')

#Задание 2.(БАЗОВЫЕ)

seconds = int(input("Введите секунды для перевода их в в часы, минуты и секунды: "))
hour = int(seconds / 3600)
minutes = int(seconds / 60)
print(f"Результат в фомате чч:мм:сс {hour}:{minutes}:{seconds}")

#Задание 3.(БАЗОВЫЕ)

number = int(input("Введите число: "))
summa = str(number) + str(number * 2) + str(number * 3)
print(summa)

#Задание 4.(БАЗОВЫЕ)

revenue = int(input("Введите значения выручки: "))
costs = int(input("Введите издержеки фирмы: "))
if revenue > costs:
    profits = revenue - costs
    profitability = profits / revenue
    people = int(input("Введите кол-во людей в фирме: "))
    profits_people = profits / people
    print(f"Прибыль составила: {profits}, Рентабильсноть: {profitability}, Прибыль на одного сотрудника: {profits_people}")
else: print("Стоит работать лучше!")