opc = input('chosen 1 option ')
var = input('variable 1')
var2 = input('variable 2')

def sumar(var, var2):
	sumar = var + var2
	return print(sumar)

while opc:
	print("1) 2) 3)")
	if opc == 1:
		print(sumar)
	else:
		print("chosen one option available")
		break


