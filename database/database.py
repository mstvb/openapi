from database.user import User
from database import *

class Database:
	def __init__(self):
		self.users = {}
		self.active = {}
		self.version = 0.2

	
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


	def checkPassword(self, username, password):
		if self.isExist(username):
			user = self.getUser(username)
			return user.password == password


	def setOnline(self, username):
		if self.isExist(username):
			if self.active[username]:
				del self.active[username]
			else:
				self.active[username] = self.users[username]


	def getUser(self, username):
		if self.isExist(username):
			return self.users[username]

		
	def getOnlinePlayers(self):
		online = []
		for player in self.active:
			online.append(self.users[player])
		return online
