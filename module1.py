a = input("Первое число: ")
b = input("Второе число: ")
c = input("Третье число: ")

numb = []

numb.append(a)
numb.append(b)
numb.append(c)

def test1():
	for elem in numb:
		max_numb = max(numb)
		min_numb = min(numb)
	print(f"Наибольшее число: {max_numb}")
	print(f"Наименьшее число: {min_numb}")

def test2():
	for elem in numb:
		numb1 = max(numb)
		if numb1 == numb[0]:
			result = float(numb1) / (float(numb[1]) - float(numb[2]))
			print(result)
			break
		elif numb1 == numb[1]:
			result = float(numb1) / (float(numb[0]) - float(numb[2]))
			print(result)
			break
		elif numb1 == numb[2]:
			result = float(numb1) / (float(numb[0]) - float(numb[1]))
			print(result)
			break

def test3():
	a = input("Первое число: ")
	b = input("Второе число: ")
	c = input("Третье число: ")
	d = input("Четвертое число: ")
	if a == d:
		print(f"Элемент: {a} равен d!")
	elif b == d:
		print(f"Элемент: {b} равен d!")
	elif c == d:
		print(f"Элемент: {c} равен d!")
	else:
		d = float(a) + float(b) + float(c)
		print(d)

def test4():
	i = 1
	result1 = 0
	while i < 11:
		i += 1
		result1 += i
	print(result1)

def test5():
	result2 = 0
	for i in range(1, 11):
		result2 += i
	print(result2)

test2()
