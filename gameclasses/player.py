from location import Location2D, Location3D
from gameclasses.inventory import Inventory

class Player2D:
	def __init__(self, x, y):
		self.loc = Location2D(x, y)
		self.inv = Inventory(32)


	def getLocation(self):
		return self.loc


	def getPlayerLocation(self):
		return self.loc.getX(), self.loc.getY()


class Player3D:
	def __init__(self, x, y, z):
		self.loc = Location3D(x, y, z)
		self.inv = Inventory(32)
	

	def getLocation(self):
		return self.loc

	
	def getPlayerLocation(self):
		return self.loc.getX(), self.loc.getY(), self.loc.getZ()