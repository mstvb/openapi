class Inventory:
	def __init__(self, size):
		self.inv = []
		self.maxsize = size


	def addItem(self, item):
		if len(self.inv) < self.maxsize:
			self.inv.append(item)
		else:
			return False


	def setItem(self, slot, item):
		if slot > self.maxsize:
			return False
		else:
			self.inv[slot] = item


	def contains(self, item):
		if item in self.inv:
			return True
		else:
			return False


	def getSlot(self, slot):
		return self.inv[slot]


	def getInventory(self):
		return self.inv