import math


class Location2D:
	def __init__(self, x, y):
		self.loc = [x, y]


	def collide(self, target, radius):
		dx = self.getPosX() - target.getLocation().getPosX()
		dy = self.getPosY() - target.getLocation().getPosY()
		dist = math.hypot(dx, dy)
		return dist < radius


	def setLocation(self, x, y):
		self.loc = [x, y]


	def setPosX(self, x):
		self.loc[0] = x


	def setPosY(self, y):
		self.loc[1] = y


	def getPosX(self):
		return self.loc[0]


	def getPosY(self):
		return self.loc[1]


	def getLocation(self):
		return self.loc


class Location3D:
	def __init__(self, x, y, z):
		self.loc = [x, y, z]


	def collide(self, target, radius):
		dx = (self.getPosX() - target.getLocation().getPosX()) * (self.getPosX() - target.getLocation().getPosX())
		dy = (self.getPosY() - target.getLocation().getPosY()) * (self.getPosY() - target.getLocation().getPosY())
		dz = (self.getPosZ() - target.getLocation().getPosZ()) * (self.getPosZ() - target.getLocation().getPosZ())
		rad = (radius + radius)
		dist = math.sqrt(dx + dy + dz)
		return dist < rad


	def setLocation(self, x, y, z):
		self.loc = [x, y, z]


	def setPosX(self, x):
		self.loc[0] = x


	def setPosY(self, y):
		self.loc[1] = y


	def setPosZ(self, z):
		self.loc[2] = z


	def getPosX(self):
		return self.loc[0]


	def getPosY(self):
		return self.loc[1]


	def getPosZ(self):
		return self.loc[2]


	def getLocation(self):
		return self.loc