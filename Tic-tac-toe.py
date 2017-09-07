n = 20
move = 0
playing_field = list()
header = list()
victory_condition_X = 0
victory_condition_O = 0

the_one_string = ""

def check_X(field):
	victory_condition_X = 0
	X_number = 0


	if field.find("X") > 0:
		j = field.find("X")
		while j>0:
			victory_condition_X = 0
			while (field[j] == "X") and (j<len(field)):
				j = j+1
				victory_condition_X = victory_condition_X + 1
			if victory_condition_X == 5:
				return (victory_condition_X)
			else:
				j = field.find("X",j+1)


	return(victory_condition_X)


def check_O(field):
	victory_condition_O = 0
	O_number = 0

	if field.find("O") > 0:
		j = field.find("O")
		while j>0:
			victory_condition_O = 0
			while (field[j] == "O") and (j<len(field)):
				j = j+1
				victory_condition_O = victory_condition_O + 1
			if victory_condition_O == 5:
				return (victory_condition_O)
			else:
				j = field.find("O",j+1)

	return(victory_condition_O)



print("WELCOME TO THE TIC--TAC--TOE 2017!")
print("First number is horizontal coordinate, second is vertical coordiante.")
print("X gets first move.")
for i in range(n):
	playing_field.append([""]*n) 

#for i in range(n):
#	header.append(i+1) 

#print(header)
for i in range(n):
	print(playing_field[i])

while (victory_condition_X < 5 ) and (victory_condition_O < 5) or (move < n**2):
	the_one_string = ""
	victory_condition_X = 0
	victory_condition_O = 0
	this_move = (str(input())).split(" ")
	horizontal = int(this_move[0])
	vertical = int(this_move[1])
	while playing_field[horizontal-1][vertical-1] != "":
		print("Taken already. Pick another position.")
		
	if move%2 == 0:
		playing_field[horizontal-1][vertical-1] = "X"
	else:
		playing_field[horizontal-1][vertical-1] = "O"
	move = move + 1
	

	for i in range(n):
		print(playing_field[i])

	for i in range(n):
		the_one_string = the_one_string + " " + ("").join(playing_field[i])

	the_one_string = the_one_string + " vertices "
	for i in range(n):
		for j in range(n):
			the_one_string = the_one_string + playing_field[j][i]
		the_one_string = the_one_string + " "

	the_one_string = the_one_string + " diags rightleft "

	for k in range(2*n-1):
			i = 0
			while i<n:
				if 0<=k-i<n:
					the_one_string = the_one_string + playing_field[i][k-i]
					i += 1 
				else:
					i += 1
			the_one_string = the_one_string + " "

	the_one_string = the_one_string + " diags leftright "

	for k in range(n-1,-n,-1):
			i = 0
			while i<n:
				if 0<=k+i<n:
					the_one_string = the_one_string + playing_field[i][k+i]
					i += 1 
				else:
					i += 1
			the_one_string = the_one_string + " "


	victory_condition_X = check_X(the_one_string)
	victory_condition_O = check_O(the_one_string)

if victory_condition_O == 5:
	print("O WON! Congratulations!")
elif victory_condition_X == 5:
	print("X WON! Congratulations!")
else:
	print("DRAW!")