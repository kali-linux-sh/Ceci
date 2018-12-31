import os, time, random, pwd

def eliminarEspacios(objeto):
		if type(objeto) == list:
			numero = 0
			for i in objeto:
				if i == " ":
					objeto.pop(numero)

				numero += 1

			return objeto

		elif type(objeto) == str:
			return str(''.join(c for c in objeto if c not in ' '))

def IsBlank(string):
	if type(string) != str:
		raise TypeError
	else:
		string = eliminarEspacios(string)
		return True if string == '' else False