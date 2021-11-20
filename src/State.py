class State:
    def __init__(self, isFinal: bool) -> None:
        self.transitions = {}
        self.isFinal = isFinal
    
    def addTransition(self, transition: str, nextState: str) -> None:
        if self.transitions.get(transition) is None:
            self.transitions[transition] = []
        
        self.transitions[transition].append(nextState)
    
    def getTransitions(self, transition) -> list:
        return self.transitions.get(transition)
