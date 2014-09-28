import sys
import getopt
import util

class CommandHandler:

	def __init__(self, args):
		self.number_of_args = len(args)
		self.accepted_args = ['info', 'io', 'git', 'download', 'search', 'install']
		self.ARGS = args
		self.info = Info()
		self.io = IO()
		self.git = Git()
		self.download = Download()
		self.grep = Grep()
		self.install = Install()

	def parse(self):
		if self.ARGS[0] == 'info':
			self.info.handle(self.ARGS)
		elif self.ARGS[0] == 'io':
			self.io.handle(self.ARGS)
		elif self.ARGS[0] == 'git':
			self.git.handle(self.ARGS)
		elif self.ARGS[0] == 'download':
			self.download.ARGS(self.ARGS)
		elif self.ARGS[0] == 'search':
			self.grep.handle(self.ARGS)
		elif self.ARGS[0] == 'package':
			self.install.handle(self.ARGS)
		else:
			print "Parse Error: ${self.ARGS[0]} not found"
			sys.exit(0)

	def initiale_parse(self):
		return verify_arg(self.ARGS[0])

	def verify_arg(self, arg):
		for aa in accepted_args:
			if arg == aa:
				return True
		return False

def main():
	cmd_handler = CommandHandler(sys.argv)

	if cmd_handler.initiale_parse():
		cmd_handler.parse()
	else:
		print "initiale parse error"
		sys.exit(0)

if __name__ == "__main__":
	main()


