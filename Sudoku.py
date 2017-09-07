
data = list()
legit_hor_numbers = [set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789')]
legit_ver_numbers = [set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789')]
legit_sq_numbers = [set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789'),set('123456789')]

with open('problem.txt', 'r+') as field:
	for line in field:
		data.append(line.rstrip().split(" "))
field.closed

def end(data):
	for i in range (9):
		for j in range (9):
			if type(data[i][j]) is set:
				return True

	return False

def check(i,j):
	if i<=2 and j<=2:
		return 0
	elif 2<j<=5 and i<=2:
		return 1
	elif 5<j<=8 and i<=2:
		return 2
	elif 2<i<=5 and j<=2:
		return 3
	elif 2<j<=5 and 2<i<=5:
		return 4
	elif 5<j<=8 and 2<i<=5:
		return 5
	elif 5<i<=8 and j<=2:
		return 6
	elif 2<j<=5 and 5<i<=8:
		return 7
	elif 5<j<=8 and 5<i<=8:
		return 8

for i in range (9):
	for j in range (9):
		if (data[i][j] != '0'): 
			legit_hor_numbers[i].discard(data[i][j])

for j in range (9):
	for i in range (9):
		if (data[i][j] != '0'): 
			legit_ver_numbers[j].discard(data[i][j])

for j in range (9):
	for i in range (9):
		if (data[i][j] != '0'): 
			legit_sq_numbers[check(i,j)].discard(data[i][j])

for i in range (9):
	for j in range (9):
		if data[i][j] == '0':
			data[i][j] = legit_hor_numbers[i] & legit_ver_numbers[j] & legit_sq_numbers[check(i,j)]

for i in range (9):
	for j in range (9):
		if type(data[i][j]) is set:
			if len(data[i][j]) == 1:
				data[i][j] = data[i][j].pop()

while end(data):
	for i in range (9):
		for j in range (9):
			if not(type(data[i][j]) is set): 
				legit_hor_numbers[i].discard(data[i][j])

	for j in range (9):
		for i in range (9):
			if not(type(data[i][j]) is set): 
				legit_ver_numbers[j].discard(data[i][j])

	for j in range (9):
		for i in range (9):
			if not(type(data[i][j]) is set): 
				legit_sq_numbers[check(i,j)].discard(data[i][j])

	for i in range (9):
		for j in range (9):
			if type(data[i][j]) is set:
				data[i][j] = legit_hor_numbers[i] & legit_ver_numbers[j] & legit_sq_numbers[check(i,j)]

	for i in range (9):
		for j in range (9):
			if type(data[i][j]) is set:
				if len(data[i][j]) == 1:
					data[i][j] = data[i][j].pop()




with open('problem.txt', 'r+') as field:
	field.seek(0,2)
	field.write('\n')
	for i in range (9):
		field.write((" ").join(data[i])+'\n')
field.closed


