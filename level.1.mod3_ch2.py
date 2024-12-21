
l = [1, 4 , 1, 6, 'hello', 'a', 5, 'hello']
duplicates = []
uniqe = []
for i in l:
	if l.count(i) > 1 and i not in duplicates:
		duplicates.append(i)

print(duplicates)
