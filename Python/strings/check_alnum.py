s=input()
l=list(s)
k=[]
for i in l:
	if i.isalnum():
		if i.isalpha() and i.islower():
			k.append(4)
		elif i.isalpha() and i.upper():
			k.append(5)
		elif i.isdigit():
			k.append(3)



if 3 in k or 4 in k or 5 in k:
	print('True')
else:
	print('False')

if 4 in k or 5 in k:
	print('True')
else:
	print('False')

if 3 in k:
	print('True')
else:
	print('False')

if 4 in k:
	print('True')
else:
	print('False')

if 5 in k:
	print('True')
else:
	print('False')