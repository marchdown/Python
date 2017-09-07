import sys
import math
user_inp = str(input())


def exp(expression):
	expression_list = list()
	current_number = str()
	for i in range(len(expression)):
		if (expression[i] == "^"):
			expression_list.append(current_number)
			expression_list.append(expression[i])
			current_number = str()
		else:
			current_number = current_number + expression[i]

	expression_list.append(current_number)

	for i in range(len(expression_list)-1,0,-1):
		if (expression_list[i] == "^"):
			expression_list[i-1] = str(float(expression_list[i-1])**float(expression_list[i+1])) 

	return expression_list[0]

def multiplication(expression):
	expression_list = list()
	current_number = str()
	for i in range(len(expression)):
		if (expression[i] == "*") or (expression[i] == "/"):
			expression_list.append(current_number)
			expression_list.append(expression[i])
			current_number = str()
		else:
			current_number = current_number + expression[i]

	expression_list.append(current_number)

	for i in range(len(expression_list)):
		for j in range(len(expression_list[i])):
			if (expression_list[i][j] == "^"):
				expression_list[i] = exp(expression_list[i])
				break

	for i in range(len(expression_list)):
		if (expression_list[i] == "*"):
			expression_list[i+1] = str(float(expression_list[i-1])*float(expression_list[i+1])) 
		elif (expression_list[i] == "/"):
			expression_list[i+1] = str(float(expression_list[i-1])/float(expression_list[i+1]))
		

	return expression_list[len(expression_list)-1]

def addition(expression):
	expression_list = list()
	current_number = str()
	for i in range(len(expression)):
		if (expression[i] == "+") or (expression[i] == "-" and expression[i-1] != "-" and expression[i-1] != "+" and expression[i-1] != "*" and expression[i-1] != "/" and expression[i-1] != "^" and i != 0):  #Some problems with logic i have
			expression_list.append(current_number)
			expression_list.append(expression[i])
			current_number = str()
		else:
			current_number = current_number + expression[i]
	
	expression_list.append(current_number)
	
	
	for i in range(len(expression_list)):
		for j in range(len(expression_list[i])):
			if (expression_list[i][j] == "*") or (expression_list[i][j] == "/") or (expression_list[i][j] == "^"):
				expression_list[i] = multiplication(expression_list[i])
				break

	for i in range(len(expression_list)):
		if (expression_list[i] == "+"):
			expression_list[i+1] = str(float(expression_list[i-1])+float(expression_list[i+1])) 
		elif (expression_list[i] == "-"):
			expression_list[i+1] = str(float(expression_list[i-1])-float(expression_list[i+1]))

	return expression_list[len(expression_list)-1]
				

def clearing(expression):
	expression = expression.replace(" ", "")
	return expression

#Main
user_inp = clearing(user_inp)

if user_inp.count("(") != user_inp.count(")"):
	raise SystemExit("BRACKET ERROR")

any_brackets = 1
while any_brackets == 1:
	current_closing_bracket_num = user_inp.find(")")
	current_opening_bracket_num = user_inp.rfind("(", 0, current_closing_bracket_num)
	if (current_opening_bracket_num == current_closing_bracket_num):
		any_brackets = 0
		current_expression = user_inp
		user_inp = addition(current_expression)
		break
	current_expression = user_inp[current_opening_bracket_num + 1:current_closing_bracket_num]
	user_inp = user_inp[0:current_opening_bracket_num] + str(addition(current_expression)) + user_inp[current_closing_bracket_num+1:len(user_inp)]
print(user_inp)
