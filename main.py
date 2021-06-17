from database import *
from gameclasses import *
from states import *
import json


# JSON File
class JLoader:
	def __init__(self, filename):
		self.filename = filename
		self.file = open(filename)
		self.jsondata = json.loads(self.file.read())


	def getFile(self):
		return self.jsondata


	def getValue(self, key):
		return self.jsondata[key]


	def setValue(self, key, value):
		self.jsondata[key] = value


	def saveFile(self):
		self.file = open(self.filename, "w")
		self.file.write(json.dumps(self.jsondata))
		self.file.close()


if __name__ == "__main__":
	j = JLoader('version.json')	
	print(f"OpenAPI: {j.getValue('version')}")
	print(f"Developed by: {j.getValue('developer')}")
