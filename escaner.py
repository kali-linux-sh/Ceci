from ast import literal_eval as str_dict
import os, random, re, time
from find import Finder
from colorama import Fore as color
from colorama import Back as fondo
from colorama import Style as estilo
from colorama import init as coloramaInit

coloramaInit(autoreset=True)

class Scanner(object):
	def __init__(self, head):
		super(Scanner, self).__init__()
		self.program_head = head
		self.keys, self.keys_cache = {}, {}
		self.extenciones_malas = [
		'dll', 'exe', 'scr', 'bat', 'com', 'pif',
		'sh', 'tar', 'zip', 'gz', 'rb', 'py']
		self.operaciones_m = [
		'rm –rf *', 'rm –rf /', 'mv ~ /dev/null', 
		'ls > /dev/sda', 'MetasploitModule', 
		'(echo cm0gLXJmIH4vKg== | base64 -d)', 
		':(){ :|: & };:', 'mv directorio/dev/null', 'mkfs', 
		'dd if=/dev/hda of=/dev/hdb', 
		'dd if=/dev/hda of=/dev/sdb',
		'dd if=something of=/dev/sda']

		self.archivos_error = []
		self.archivos_bajos = []
		self.archivos_altos = []

	def _abrir_keys(self):
		if os.path.exists('keys.Ckeys'):
			a = open('keys.Ckeys', 'r').read()
			self.keys = str_dict(a)

	def escaner(self, ruta=None):
		archive = False
		if ruta == None:
			archive = True
			a = input("Ingrese la ruta: " + self.program_head.usuario['ruta'] + "/")
			ruta = self.program_head.usuario['ruta'] + "/" + a
		try:
			texto = open(ruta, 'r').read()
			texto.encode('utf-8').decode('utf-8')
			for palabra in self.operaciones_m:
				patron = re.compile(r'\b' + palabra + r'\b')
				if patron.search(texto):
					if not ruta in self.archivos_altos:
						self.archivos_altos.append(ruta)
		except Exception:
			if not archive:
				self.archivos_error.append(ruta)
			else:
				input("Hubo problemas para analizar el archivo.")
				self.program_head.console('clear')

		if archive:
			if ruta in self.archivos_altos:
				input(color.RED + "El archivo es peligroso!" + color.RESET)
				self.archivos_altos = []
			else: input(color.GREEN + "El archivo no es peligroso." + color.RESET)		

	def scan(self, ruta=None):
		key = self.create_keys()
		status = ''

		ruta = self.program_head.usuario['ruta'] if ruta == None else ruta
		for base, dirs, files in os.walk(ruta):
			for element in files:
				extencion = element.split('.')[1] if '.' in element else None
				if extencion in self.extenciones_malas:
					print(base + "/" + element)
					if not (base + "/" + element) in self.archivos_bajos: 
						self.archivos_bajos.append(str(base + '/' + element))
						self.escaner(base + "/" + element)

		time.sleep(0.3)
		self.program_head.console('clear')

		input(fondo.GREEN + "El escaneo se realizo con exito..." + fondo.RESET)

		if not (self.archivos_bajos + self.archivos_altos):
			input(color.GREEN + "No tiene virus detectado!" + color.RESET)
			self.program_head.console('clear')
			status = 'exelente'
		
		if self.archivos_altos:
			input(color.RED + "Archivos que debe revisar:" + color.RESET)
			for i in self.archivos_altos:
				print("- " + i)
				time.sleep(0.4)
			status = 'Malo'

		if self.archivos_bajos:
			input(color.YELLOW + "Archivos que son menos peligrosos:" + color.RESET)
			for i in self.archivos_bajos:
				if i in self.archivos_altos:
					pass
				print("- " + i)
				time.sleep(0.4)
			status = 'Aceptable'

		if self.archivos_error:
			input(color.WHITE + fondo.RED + "Estos archivos causaron error:" + color.RESET + fondo.RESET)
			for i in self.archivos_error:
				print("- " + i)
				time.sleep(0.4)

		self.keys_cache[key] = {
		'status':status,
		'usuario':self.program_head.usuario['nombre'],
		'ruta':ruta,
		'posibles virus':self.archivos_altos,
		'archivos dudosos':self.archivos_bajos
		}
		self.archivos_bajos = []
		self.archivos_altos = []
		self.archivos_error = []

	def create_keys(self):
		key = ""
		numeros = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
		for i in range(0, 21):
			key += random.choice(numeros)

		if key in self.keys or key in self.keys_cache:
			self.create_keys()
		else:
			return str('<' + key + '>')

	def show_keys_t(self):
		print(fondo.YELLOW + "Keys temporales:" + fondo.RESET)
		for key in self.keys_cache:
			print(key)
		print("-" * 19)
		input(fondo.YELLOW + color.RED + "Presione ENTER para volver al menu..." +  fondo.RESET + color.RESET)
		self.program_head.console('clear')

	def show_keys_g(self):
		print(fondo.GREEN + "Keys guardadas:" + fondo.RESET)
		for key in self.keys:
			print(key)
		print("-" * 19)
		input(fondo.YELLOW + color.RED + "Presione ENTER para volver al menu..." +  fondo.RESET + color.RESET)
		self.program_head.console('clear')

	def save_key(self):
		name = input("Ingrese la key a guardar: ")
		try:
			self.keys[name] = self.keys_cache[name]
			print(color.GREEN + "Key guardada!" + color.RESET)
			self.program_head.console('clear')
		except Exception:
			print(color.RED + "La Key no existe!" + color.RESET)
			self.program_head.console('clear')

	def save_keys(self):
		for i in self.keys_cache:
			self.keys[i] = self.keys_cache[i]