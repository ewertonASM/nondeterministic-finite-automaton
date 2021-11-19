import fire


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
        
    parsed_list.append(["transicoes", transitions_list])
    
    return parsed_list
        
def process(file=str):
    
    try:
        with open(file) as f:
            lines = [line.strip() for line in f.readlines()]
            data = {parsed_line[0]:parsed_line[1] for parsed_line in entry_parser(lines)}
            
            
            
    except print(0):
        pass
    
    
        
        
    
    print(data)

if __name__ == '__main__':
    fire.Fire(process)
    
    