numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABETS = [x.upper() for x in alphabets]
punctuations = [';', '(', ')', '{', '}', '.', '-', '+', '*', '/', '<', '>', '=', '&', '|', '!']

def dfa(string):
	count = -1
	state = ""
	if len(string) == 1:
		if string[0] == ';':
			token = "<Semicolon>"
			return token
		elif string[0] == '(':
			token = "<L_paren>"
			return token
		elif string[0] == ')':
			token = "<R_paren>"
			return token
		elif string[0] == '{':
			token = "<L_brace>"
			return token
		elif string[0] == '}':
			token = "<R_brace>"
			return token
		elif string[0] == '.':
			token = "<Dot_OP>"
			return token
		elif string[0] == '-':
			token = "<Sub_OP>"
			return token
		elif string[0] == '+':
			token = "<Add_OP>"
			return token
		elif string[0] == '*':
			token = "<Mul_OP>"
			return token
		elif string[0] == '/':
			token = "<Div_OP>"
			return token
		elif string[0] == '<':
			token = "<Less than>"
			return token
		elif string[0] == '>':
			token = "<Greater than>"
			return token
		elif string[0] == '&':
			token = "<Logical AND>"
			return token
		elif string[0] == '|':
			token = "<Logical OR>"
			return token
		elif string[0] == '!':
			token = "<Logical NOT>"
			return token
		elif string[0] == '=':
			token = "<Assig_OP>"
			return token
		else:
			state = "notFound"
	elif len(string) == 2:
		if string[0] == 'i':
			if string[1] == 'f':
				token = "<if>"
				return token
			else:
				state = "notFound"
		elif string[0] == '<':
			if string[1] == '=':
				token = "LE"
				return token
			else:
				state = "notFound"
		elif string[0] == '>':
			if string[1] == '=':
				token = "GE"
				return token
			else:
				state = "notFound"
		elif string[0] == '=':
			if string[1] == '=':
				token = "<Equal(if condition)>"
				return token
			else:
				state = "notFound"
		elif string[0] == '!':
			if string[1] == '=':
				token = "<Not Equal>"
				return token
			else:
				state = "notFound"
		else:
			state = "notFound"
	elif len(string) == 3:
		if string[0] == 'i':
			if string[1] == 'n':
				if string[2] == 't':
					token = "<int>"
					return token
				else:
					state = "notFound"
			else:
				state = "notFound"
		elif string[0] == 'f':
			if string[1] == 'o':
				if string[2] == 'r':
					token = "<for>"
					return token
				else:
					state = "notFound"
			else:
				state = "notFound"
		else:
			state = "notFound"
	elif len(string) == 4:
		if string[0] == 'e':
			if string[1] == 'l':
				if string[2] == 's':
					if string[3] == 'e':
						token = "<else>"
						return token
					else:
						state = "notFound"
				else:
					state = "notFound"
			else:
				state = "notFound"
		else:
			state = "notFound"
	elif len(string) == 5:
		if string[0] == 'f':
			if string[1] == 'l':
				if string[2] == 'o':
					if string[3] == 'a':
						if string[4] == 't':
							token = "<float>"
							return token
						else:
							state = "notFound"
					else:
						state = "notFound"
				else:
					state = "notFound"
			else:
				state = "notFound"
		elif string[0] == 'w':
			if string[1] == 'h':
				if string[2] == 'i':
					if string[3] == 'l':
						if string[4] == 'e':
							token = "<while>"
							return token
						else:
							state = "notFound"
					else:
						state = "notFound"
				else:
					state = "notFound"
			else:
				state = "notFound"
		else:
			state = "notFound"
	elif len(string) == 6:
		if string[0] == 's':
			if string[1] == 't':
				if string[2] == 'r':
					if string[3] == 'i':
						if string[4] == 'n':
							if string[5] == 'g':
								token = "<string>"
								return token
							else:
								state = "notFound"
						else:
							state = "notFound"
					else:
						state = "notFound"
				else:
					state = "notFound"
			else:
				state = "notFound"
		else:
			state = "notFound"
	else:
		state = "notFound"
	if state == "notFound":
		if string[0] in numbers:
			i = 0
			while i != len(string):
				if string[i] == '.':
					if count < 0:
						count += 1
						i += 1
					else:
						token = "error"
						return token
				elif string[i] not in numbers:
					token = "error"
					return token
				else:
					i += 1
			if i == len(string):
				number = "".join(string)
				token = "<number, %s>" % number
				return token
		if string[0] in alphabets or string[0] in ALPHABETS:
			i = 0
			while i != len(string):
				if string[i] == '_':
					i += 1
				elif (string[i] not in alphabets and string[i] not in numbers) and string[i] not in ALPHABETS:
					token = "error"
					return token
				else:
					i += 1
			if i == len(string):
				number = "".join(string)
				token = "<id, %s>" % number
				return token
		if string[0] == '"':
			i = 0
			count = -1
			while i != len(string):
				if string[i] == '"':
					if count < 2:
						count += 1
						i += 1
					else:
						token = "error"
						return token		
				else:
					i += 1
			if i == len(string):
				number = "".join(string)
				token = "<literal, %s>" % number
				return token

def main():
	file = open('input_code.txt', 'r')
	lineNumber = 1
	table = []
	string = []
	symbol = []
	errorLine = []
	tokens = []
	for j in range(3):
	    row = []
	    for i in range(10):
	        row.append(-1)
	    table.append(row)
	# for i in range(10):
	#     print()
	#     for j in range(3):
	#         print(table[j][i], end="\t")
	# print()
	while 1:
		char = file.read(1)
		if char == '\n':
			lineNumber += 1
		if char in punctuations:
			symbol.append(char)
		if char != ' ' and char != '\n' and char != '\t' and (char not in punctuations or char == '.'):
			string.append(char)
		if char == ' ' or char == '\n' or char == '\t' or (char in punctuations and char != '.'):
			if len(string) != 0:
				token = dfa(string)
				if token == "error":
					errorLine.append(lineNumber)
					token = None
				elif token != None:
					tokens.append(token)
					token = None
			string.clear()
		if char in alphabets or char in ALPHABETS or char in numbers or char == '\t' or char == '\n' or char == ' ':
			if len(symbol) != 0:
				token = dfa(symbol)
				if token != None:
					tokens.append(token)
					token = None
			symbol.clear()
		if not char:
			break
	print(tokens)
	print()
	for i in errorLine:
		print(f"<error, line number {i}>")
	file.close()

main()