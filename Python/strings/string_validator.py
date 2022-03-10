if __name__ == '__main__':
	s = input()
	listOfString = list(s)
	listofkeys = []
	for i in listOfString:
		if i.isalnum():
			listofkeys.append(1)
		elif i.isalpha():
			listofkeys.append(2)
		elif i.isdigit():
			listofkeys.append(3)
		elif i.islower():
			listofkeys.append(4)
		elif i.isupper():
			listofkeys.append(5)
	
	if 1 in listofkeys:
		print('True')
	else:
		print('False')

	if 2 in listofkeys:
		print('True')
	else:
		print('False')

	if 3 in listofkeys:
		print('True')
	else:
		print('False')
	
	if 4 in listofkeys:
		print('True')
	else:
		print('False')

	if 5 in listofkeys:
		print('True')
	else:
		print('False')


		