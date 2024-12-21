a = float(input('Размер стороны a: '))
b = float(input('Размер стороны b: '))
c = float(input('Размер стороны c: '))

def area (a, b, c):
	s = (a + b + c) / 2 
	area = (s * (s - a) * (s - b) * (s - c)) ** 0,5
	return s

print('Площадь труегольника', area (a, b, c))



