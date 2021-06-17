from gameclasses.location import Location2D, Location3D


class Entity2D:
	def __init__(self, x=0, y=0):
		self.loc = Location2D(x, y)


	def getLocation(self):
		return self.loc


	def getEntityLocation(self):
		return self.loc.getLocation()


class Entity3D:
	def __init__(self, x=0, y=0, z=0):
		self.loc = Location3D(x, y, z)


	def getLocation(self):
		return self.loc


	def getEntityLocation(self):
		return self.getLocation()