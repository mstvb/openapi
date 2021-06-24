class StateLoader:
    def __init__(self):
        """
        Loader Class for States
        """
        self.currentstate = None
        self.states_id = []
        self.states = {}


    def setStatewithID(self, stateID: int):
        if not stateID: # Parameter ist nicht ausgefüllt.
            return
        if self.currentstate is not None:
            self.currentstate.stop()
        try:
            self.currentstate = self.states_id[stateID]
            self.currentstate.start()
        except:
            return False


    def setStatewithName(self, stateName: str):
        if not stateName:
            return
        if self.currentstate is not None:
            self.currentstate.stop()
        try:
            self.currentstate = self.states[stateName]
            self.currentstate.start()
        except:
            return False


    def stopState(self):
        try:
            if self.currentstate is not None:
                self.currentstate.stop()
        except:
            return False


    def addState(self, state):
        if not state: # Parameter ist nicht ausgefüllt.
            return
        if "stop" not in dir(state) and "start" not in dir(state):
            return
        self.states_id.append(state)
        self.states[state.getName()] = state


    def removeState(self, stateID):
        if not stateID:
            return
        try:
            self.states_id.pop(stateID)
            del self.states[self.states_id[stateID].getName()]
        except:
            return False


    def getStates(self):
        return self.states_id


    def getStateName(self, stateID: int):
        if not stateID: # Parameter ist nicht ausgefüllt.
            return
        try:
            return self.states_id[stateID].getName()
        except:
            return False