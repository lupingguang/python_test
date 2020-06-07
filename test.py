import pyperclip

catNames = []
while True:
	print('Enter the name of cat ' + str(len(catNames) + 1) +
	' (Or enter nothing to stop.):')
	name = input()
	if name == '':
		break
	catNames = catNames + [name] # list concatenation
	print('The cat names are:')
	for i in range(len(catNames)):
		print(' ' + catNames[i])
	#pyperclip.copy(catNames[0])
	print(pyperclip.paste())