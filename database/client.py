from database.database import Database


class Client:
	def __init__(self):
		self.database = Database() # Database for Players
		self.version = 0.1 # Client Version
		self.user = None # User


	def register(self, username, password):
		self.database.addUser(username, password)
		self.user = self.database.getUser(username)


	def unregister(self):
		self.database.removeUser(self.user.getUsername())


	def checkVersion(self):
		if self.database.version > self.version:
			print("Your client is outdated")
		else:
			print("update for your client doesn't exist")