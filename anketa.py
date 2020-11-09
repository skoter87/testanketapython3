name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = int(input('Введите ваш возраст: '))
weight = int(input('Введите ваш вес: '))

if age < 30 and (weight > 50 or weight < 120):
	print('Вы в отличном состоянии!')
elif age >= 40 and (weight <= 50 or weight >= 120):
	print('Вам стоит пойти к врачу!')
elif age <= 20 and (weight > 35 or weight < 70):
	print('Здоровье студента в хорошем состоянии')
print('Имя пациента:'+ name)
print('Фамилия пациента:' + surname)
print('Возраст пациента:' + str(age))
print('Вес пациента:' + str(weight))