from colorama import Fore as color
from colorama import Back as fondo
from colorama import Style as estilo
from colorama import init as coloramaInit

coloramaInit(autoreset=True)

class Error(Exception):
	def __init__(self, msj, emisor, *args):

		cadena = color.RED + msj + ": " + color.RESET + str(emisor)
		print(cadena)

		if args:

			self.argumentos = args
			print(color.YELLOW + "La aplicación dejo algunos mensajes para tí: ")
			for i in self.argumentos:
				print("	-" + i)

		input(color.RED + fondo.YELLOW + "Presione enter para continuar..." + fondo.RESET + color.RESET)

