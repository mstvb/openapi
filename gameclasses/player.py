from gameclasses.inventory import Inventory
from gameclasses.location import Location2D, Location3D


class Player2D:
	def __init__(self, x=0, y=0):
		self.loc = Location2D(x, y)
		self.inv = Inventory(32)


	def getInventory(self):
		return self.inv


	def getPlayerInventory(self):
		return self.inv.getInventory()


	def getLocation(self):
		return self.loc


	def getPlayerLocation(self):
		return self.loc.getLocation()


class Player3D:
	def __init__(self, x=0, y=0, z=0):
		self.loc = Location3D(x, y, z)
		self.inv = Inventory(32)

	
	def getInventory(self):
		return self.inv


	def getPlayerInventory(self):
		return self.inv.getInventory()
	

	def getLocation(self):
		return self.loc


	def getPlayerLocation(self):
		return self.loc.getLocation()