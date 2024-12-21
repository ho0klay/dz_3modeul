
x = float(input('Введите начальный вклад(сумма):'))
p = float(input('годовой процент:'))
y = float(input('Итоговая сумма(цель):'))

years = 0
while x < y:
	x *= 1 + p/ 100
	x = int(100 * x) / 100
	years += 1
print(years)   
