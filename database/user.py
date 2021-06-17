class User:
	def __init__(self, username, password):
		self.userdata = {}
		self.userdata["username"] = username
		self.userdata["password"] = password
		self.userdata["loggedIn"] = False


	def setLoggedIn(self):
		if self.userdata["loggedIn"]:
			self.userdata["loggedIn"] = False
		else:
			self.userdata["loggedIn"] = True


	def setUsername(self, username):
		self.userdata["username"] = username

	
	def setPassword(self, password):
		self.userdata["password"] = password


	def getUsername(self):
		return self.userdata["username"]


	def getPassword(self):
		return self.userdata["password"]

	
	def getLoggedIn(self):
		return self.userdata["loggedIn"]
