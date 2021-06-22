class StateLoader:
	def __init__(self):
		self.states = dict()
		self.current_state = None


	def addState(self, state):
		if "start" and "stop" in dir(state):
			self.states[state.getStateName()] = state
		else:
			return


	def setState(self, stateName):
		if stateName in self.states:
			self.current_state = self.states[stateName]
			if type(self.current_state) == type(int):
				self.current_state.start()


	
	def stopState(self):
		self.current_state.stop()
	
			
