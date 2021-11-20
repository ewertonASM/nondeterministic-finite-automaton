import fire


from os import path, stat
from ProcessState import ProcessState
from State import State
from EntryValidator import EntryValidator



def entry_parser(lines=list):
    
    parsed_list = []
    transitions_list = []
    transitions_flag = False
    
    for line in lines:
        
        if line == "transicoes":
            transitions_flag = True
            continue
            
        if transitions_flag:
            transitions_list.append(line.split(","))
            
        else:
            splited_line = line.split("=")
            parsed_list.append([splited_line[0], splited_line[1].split(",")])
      
    if transitions_list:  
        parsed_list.append(["transicoes", transitions_list])
    
    return parsed_list
        
def process(file=str):
    
    try:
        with open(file) as f:
            lines = [line.strip() for line in f.readlines()]
            data = {parsed_line[0]:parsed_line[1] for parsed_line in entry_parser(lines)}   
            
    except Exception:
        
        print("Could not process the file")
        raise SystemExit(1)
    
    errors = EntryValidator().validator_with_tag(data=data)
    
    if errors:
        print("errors found:")
        for error in errors: print(error)
    else:
        print(data)

    states = {}
    for state in data["estados"]:
        states[state] = State(state in data["finais"])

    for transition in data["transicoes"]:
        states[transition[0]].addTransition(transition[2], transition[1])
    
    sequence = input("Digite a sua cadeia: ")
    # sequence = "abbb"
    processStates = []
    sequence = list(sequence.strip());
    currentState = ProcessState(data["inicial"][0], [], sequence)
    processStates.append(currentState)

    print("Alfabeto:", data["alfabeto"])
    print("Estados:", data["estados"])
    print("Estado inicial:", data["inicial"])
    print("Estados finais:", data["finais"])
    print("Sequence:", sequence)
    
    print()

    while len(processStates) > 0:
        currentState = processStates.pop(0)

        if len(currentState.sequence) == 0:
            currentState.printPath(states[currentState.key].isFinal)
            continue
    
        transition = currentState.sequence.pop(0)
        stateTransitions = states[currentState.key].getTransitions(transition)

        if stateTransitions is None:
            stateTransitions = states[currentState.key].getTransitions("episilon")
            if stateTransitions is None:
                currentState.printPath(False)
                continue
        
        for state in stateTransitions:
            newState = ProcessState(state, currentState.path, currentState.sequence)
            processStates.append(newState)
        

if __name__ == '__main__':
    fire.Fire(process)
    
    