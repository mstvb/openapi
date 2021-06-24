import types


class StateTemplate:
    def __init__(self, state_name, start_function, stop_function):
        """
        Template Class for State

        :param state_name: Name des States
        :param start_function: Funktion wenn der State gestartet wird
        :param stop_function: Funktion wenn der State gestoppt wird
        """
        if type(start_function) is type(types.FunctionType):
            self.start_function = start_function
        else:
            self.start_function = lambda: 0
        if type(stop_function) is type(types.FunctionType):
            self.stop_function = stop_function
        else:
            self.stop_function = lambda: 0
        if state_name == "":
            return
        else:
            self.state_name = state_name
            self.start_message = "Started " + state_name
            self.stop_message = "Stopped " + state_name


    def start(self):
        print(self.start_message)
        self.start_function()

    def stop(self):
        print(self.stop_message)
        self.stop_function()

    def getName(self):
        return self.state_name
