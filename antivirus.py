import os, time, random, pwd
from progress.bar import Bar, ChargingBar
from error import Error
from colorama import Fore

class Antivirus(object):
	def __init__(self):
		try:
			input = raw_input
		except Exception as e:
			pass

	def __null__(self):
		return 0
		
	def init__(self, escaner, funciones):

		#Datos del usuario
		self.console = lambda x: os.system(x)
		self.usuario = {
		'nombre':pwd.getpwuid(os.getuid()).pw_name,
		'ruta':pwd.getpwuid(os.getuid()).pw_dir,
		'shell':pwd.getpwuid( os.getuid() ).pw_shell
		}

		self.logo = """
  _________  _________  __________  _________
 |  _______||  _______||  ________||___   ___|
 | |        | |        | |             | |
 | |        | |_______ | |             | |
 | |        |  _______|| |             | |
 | |        | |        | |             | |
 | |_______ | |_______ | |________  ___| |___
 |_________||_________||__________||_________|
"""

		super(Antivirus, self).__init__()
		self.escaner = escaner
		self.funciones = funciones

	def __run(self):
		os.system("clear")

		acciones = {
		'8':self.salir,
		'1':self.escaner.scan,
		'2':self.escanear,
		'3':self.escaner.escaner,
		'4':self.escaner.show_keys_t,
		'5':self.escaner.save_keys,
		'6':self.escaner.show_keys_g,
		'7':self.escaner.save_key
		}

		while True:
			print(self.logo)
			try:
				opcion = self.menu()
			except KeyboardInterrupt:
				self.salir()
			except EOFError:
				Error("Se genero un error de EOFError", self,
				"Esto obliga al programa a cerrarse.")
				self.salir()
			except OSError:
				Error("Error del modulo OS de python", self)

			opcion = self.funciones.eliminarEspacios(opcion)

			if opcion in acciones:
				acciones[opcion]()
			elif self.funciones.IsBlank(opcion):
				self.console('clear')
			else:
				print(opcion)
				Error("Opción Incorrecta", self)
				self.console("clear")

	def escanear(self):
		a = input("-> Directorio: " + self.usuario['ruta'] + '/')
		a = self.funciones.eliminarEspacios(a)
		if os.path.exists(self.usuario['ruta'] + '/' + a):
			self.escaner.scan(self.usuario['ruta'] + '/' + a)
		else:
			self.console('clear')

	def salir(self):
		tokens = str(self.escaner.keys)
		a = open('keys.Ckeys', 'w').write(str(tokens))
		os.system("clear")
		exit(0)

	def run(self):
		print(self.logo)
		barra = ChargingBar('Leyendo configuración:', max=10)

		for i in range(11):
			time.sleep(0.4)
			barra.next()

		self.escaner._abrir_keys()
		barra.finish()
		self.console("clear")
		self.__run()


	def menu(self):
		menu = """
[1]- Escanear todo
[2]- Escanear directorio especifico
[3]- Escanear archivo
[4]- Revisar keys temporales
[5]- Guardar keys
[6]- Mostrar keys guardadas
[7]- Guardar key especifica
[8]- Salir
"""
		print(menu)
		return str(input("[--> "))