import subprocess
import platform
import os

def run(self, c):
	# run a shell command, c -> must be a list
	subprocess.call(c)

def software_exists(self, name):
	if run(['which', name]) == 0:
		return True
	else:
		return False

class Info:

	def handle(self, args):
		if args[1] == 'os':
			print os_name()
		if args[1] == 'machine':
			print machine()
		if args[1] == 'processor':
			print processor()
		if args[1] == 'gfxcard':
			print gfx_card_info()

	def os_name(self):
		return platform.system()

	def machine(self):
		return platform.machine()

	def processor(self):
		return platform.processor()

	def gfx_card_info(self):
		run(["lspci | grep", "-i", "--color", "'vga|3d|2d'"])

	def software_exists(self, name):
		if run(['which', name]) == 0:
			return True
		else:
			return False

class IO:

	def handle(self, args):
		if args[1] == 'copy':
			if os.path.isfile(args[2]): 
				if os.path.isdir(args[3]):
					copy(args[2], args[3])
				else:
					 print 'IO Error: Directory does not exist'
			else:
				print 'IO Error: File does not exist'
		if args[1] == 'move':
			if os.path.isfile(args[2]): 
				if os.path.isdir(args[3]):
					move(args[2], args[3])
				else:
					 print 'IO Error: Directory does not exist'
			else:
				print 'IO Error: File does not exist'
		if args[1] == 'delete':
			delete(args[2])
		if args[1] == 'clean-trash':
			print clean_trash()
		if args[1] == 'make-install':
			make_install()

	def copy(self, fr, to):
		run(['sudo cp', fr, to])

	def move(self, fr, to):
		run(['sudo mv', fr, to])

	def delete(self, f):
		if os.path.isfile(f):
			run(['sudo rm', f])
		else if os.path.isdir(f):
			run(['sudo rm', '-rf', f])
	
	def clean_trash(self):
		run(['rm', '-rf', '~/.local/share/Trash/files'])
		run(['rm', '-rf', '~/.local/share/Trash/info'])

	def make_install(self):
		run(['sudo make'])
		run(['sudo make', 'install'])

class Git:

	def handle(self, args):
		pass

	def setup(self, usr, email):
		run(['git', 'config', '--global', 'user.name', usr])
		run(['git', 'config', '--global', 'user.email', email])

	def clone(self, url, path):
		run(['git', 'clone', url, path])

class Download:

	def handle(self, args):
		pass

	def wget(self, url):
		run(['wget', url])

class Grep:

	def handle(self, args):
		pass

	def search_file(self, text, f):
		# search a file
		run(['grep', text, f])

	def search_command_output(self, cmd, text):
		# search the output of any shell command
		run(cmd.extend(["| grep", text]))

	def search_recursivly(self, path, text):
		# Search all files in a folder
		run(['grep', '-r', text, path])

class Install:

	# Manipulate the software packages on system

	def __init__(self):
		self.apt = Apt()
		self.yum = Yum()
		self.emerge = Emerge()
		self.pacman = Pacman()

	def handle(self, args):

		if software_exists('apt-get'):

			if args[1] == 'install' and args[1] == '-i':
				self.apt.install(args[2])
			if args[1] == 'remove' and args[1] == '-r':
				self.apt.remove(args[2])
			if args[1] == 'update' and args[1] == '-ud':
				self.apt.update()
			if args[1] == 'upgrade' and args[1] == '-ug':
				self.apt.upgrade()
			if args[1] == 'clean' and args[1] == '-c':
				self.apt.clean()	
	
		elif software_exists('yum'):

			if args[1] == 'install' and args[1] == '-i':
				self.yum.install(args[2])
			if args[1] == 'remove' and args[1] == '-r':
				self.yum.remove(args[2])
			if args[1] == 'update' and args[1] == '-ud':
				self.yum.update()

		elif software_exists('emerge'):

			if args[1] == 'install' and args[1] == '-i':
				self.emerge.install(args[2])
			if args[1] == 'update' and args[1] == '-ud':
				self.emerge.update()

		elif software_exists('pacman'):

			if args[1] == 'install' and args[1] == '-i':
				self.pacman.install(args[2])
			if args[1] == 'remove' and args[1] == '-r':
				self.pacman.remove(args[2])
			if args[1] == 'update' and args[1] == '-ud':
				self.pacman.update()

	class Apt:
	
		def install(self, package_name):
			run(['sudo apt-get', 'install', package_name])

		def remove(self, package_name)
			run(['sudo apt-get', 'remove', package_name])

		def clean(self):
			run(['sudo apt-get', 'autoremove'])

		def update(self):
			run(['sudo apt-get', 'update'])

		def upgrade(self):
			run(['sudo apt-get', 'update'])

	class Yum:

		def install(self, package_name):
			run(['sudo yum', 'install', package_name])

		def update(self):
			run(['sudo yum', 'update'])

		def remove(self, package_name)
			run(['sudo yum', 'remove', package_name])

	class Emerge:

		def install(self, package_name):
			run(['sudo emerge', package_name])

		def update(self):
			run(['sudo emerge', '--update', '--deep', 'world'])

	class Pacman:

		def install(self, package_name):
			run(['sudo pacman', '-S', package_name])

		def remove(self, package_name)
			run(['sudo pacman', '-R', package_name])
	
		def update(self):
			run(['sudo pacman', '-Syu'])


	
