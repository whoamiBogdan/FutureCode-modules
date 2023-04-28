#!/usr/bin/python3

nums = (2,3,5,2)

def func1(n):
	num = []
	for i in range(1, n+1):
		num.append(i)
	print(num)

def func2(w):
	name = []
	surname = []
	fath = []
	a = w.split()
	for i in a[0]:
		name.append(i)
	for x in a[1]:
		surname.append(x)
	for y in a[2]:
		fath.append(y)
	print(f"{name[0]}.{surname[0]}.{fath[0]}.")

def func3(nums):
	import numpy as np
	print(np.prod(nums))

def func4(w1, w2):
	if len(w1) == len(w2):
		print(True)
	else:
		print(False)

def func5():
	regions = ['Томская область', 'Московская область', 'Ленинградская область']
	cities = ['Томск', 'Москва', 'Санкт-Петербург']
	pop = [1051, 8594, 2027]

	a = (f"{regions[0]}: main city {cities[0]}. population {pop[0]}")
	b = (f"{regions[1]}: main city {cities[1]}. population {pop[1]}")
	c = (f"{regions[2]}: main city {cities[2]}. population {pop[2]}")

	print(a,'\n',b,'\n',c)
