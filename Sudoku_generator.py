import random

data = [[set('123456789') for j in range (9)] for i in range(9)]
coordinates = set()
for i in range (9):
	for j in range (9):
		coordinates.add((i,j))

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

while end(data):
	nochange = True

	for i in range (9):
		for j in range (9):
			if type(data[i][j]) is set:
				if len(data[i][j]) == 1:
					data[i][j] = data[i][j].pop()
					coordinates.remove((i,j))
					nochange = False

	if nochange:
		new_coord = random.sample(coordinates, 1)[0]
		i = new_coord[0]
		j = new_coord[1]
		coordinates.remove(new_coord)
		data[i][j] = data[i][j].pop()
		for k in range (9):
			if k != j: 
				if type(data[i][k]) is set:
					data[i][k].discard(data[i][j])
		for k in range (9):
			if k != i:
				if type(data[k][j]) is set:
					data[k][j].discard(data[i][j])
#		for k in range (9):
#			for l in range (9):
#				if check(k,l) == check(i,j):
#					if (k != i) or (l != j):
#						if type(data[k][l]) is set:
#							data[k][l].discard(data[i][j])


with open('sudoku.txt', 'w+') as field:
	field.seek(0,2)
	for i in range (9):
		field.write((" ").join(data[i])+'\n')
field.closed



