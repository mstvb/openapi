import types

class StateTemplate:
	def __init__(self, state_name, start_function, stop_function):
		if state_name == "" or type(state_name) is not type(str):
			self.name = "State"
		else:
			self.name = state_name 
			

		if isinstance(start_function, types.FunctionType):
			self.start_function = start_function
		else:
			self.start_function = lambda: print(f"{self.name} start function")


		if isinstance(stop_function, types.FunctionType):
			self.stop_function = stop_function
		else:
			self.stop_function = lambda: print(f"{self.name} stop function")


	def start(self):
		print(f"{self.name} started")
		self.start_function()

	
	def stop(self):
		print(f"{self.name} stopped")
		self.stop_function()


	def getStateName(self):
		return self.name