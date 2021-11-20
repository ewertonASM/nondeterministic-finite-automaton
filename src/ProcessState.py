from copy import deepcopy

class ProcessState:
    def __init__(self, key: str, path: list, sequence: list) -> None:
        self.key = key
        self.path = deepcopy(path)
        self.path.append(key)
        self.sequence = deepcopy(sequence)

    def printProcessState(self) -> None:
        print("key:", self.key, "path:", self.path, "sequence:", self.sequence)
    
    def printPath(self, accept: bool) -> None:
        if (accept):
            print("Accepted:", '->'.join(self.path))
        else:
            print("Rejected:", '->'.join(self.path))