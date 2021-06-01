from database.user import User

class Database:
	def __init__(self):
		self.users = {}
		self.active = {}

	
	def addUser(self, username, password):
		self.users[username] = User(username, password)


	def removeUser(self, username):
		if self.isExist(username):
			del self.users[username]


	def isExist(self, username):
		if self.users[username]:
			return True
		else:
			return False


	def setOnline(self, username):
		if self.isExist(username):
			if self.active[username]:
				del self.active[username]
			elif not self.active[username]:
				self.active[username] = self.users[username]


	def getUser(self, username):
		if self.isExist(username):
			return self.users[username]

		
	def getOnlinePlayers(self):
		online = []
		for player in self.active:
			online.append(self.users[player])
		return online
