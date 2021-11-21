import re

class EntryValidator:
    
    def __init__(self):
        
        self.mandatory_entries = {"alfabeto","estados","inicial", "transicoes"}
        
        self.compositions = {
            "alfabeto": ["episilon"],
            "estados": [],
        }
        
        self.compositions_rule = {
            "iniciais": "estados",
            "finais": "estados",
        }
        
        self.patterns = {
            "alphabet": r'^[a-z]$|^epsilon$',
            "states": r'^q[0-9]+$',
            "transition": r'^q[0-9]+q[0-9]+[a-z]$|^q[0-9]+q[0-9]+episilon$'
        }
        
        self.validate_rules = {
            
            "alfabeto": {"pattern":self.patterns["alphabet"], "lenght": 1},
            "estados": {"pattern":self.patterns["states"], "lenght": 1},
            "inicial": {"pattern":self.patterns["states"], "lenght": 1},
            "finais": {"pattern":self.patterns["states"], "lenght": 0},
            "transicoes": {"pattern": self.patterns["transition"], "lenght": 3}
        }
        
        self.validate_type = {
            
            "alfabeto": [self.valid_pattern, self.valid_min_lenght],
            "estados": [self.valid_pattern, self.valid_min_lenght],
            "inicial": [self.valid_pattern, self.valid_exact_lenght],
            "finais": [self.valid_pattern, self.valid_min_lenght],
            
        }
    
    def valid_pattern(self, key, values):
        
        for value in values:
        
            if not re.search(self.validate_rules[key]["pattern"], value):
                return False
            
            if key in self.compositions_rule:
                if not value in self.compositions[self.compositions_rule[key]]:
                    return False
        
        return True
    
    def valid_exact_lenght(self, key, values):
        
        return len(values) == self.validate_rules[key]["lenght"]
    
    def valid_min_lenght(self, key, values):
        
        return len(values) >= self.validate_rules[key]["lenght"]
    
    def valid_transitions(self, key, values):
        
        if len(values) == self.validate_rules[key]["lenght"]:
            return values[0] in self.compositions["estados"] \
                    and values[1] in self.compositions["estados"] \
                    and values[2] in self.compositions["alfabeto"] \
                    and re.search(self.patterns["transition"], "".join(values))
                    
        return False
        
    def validator_with_tag(self, data=dict):
        
        if not self.mandatory_entries.issubset(set(data.keys())):
            return list(self.mandatory_entries-set(data.keys()))
                
        errors = []
        
        for key,values in data.items():
            
            if key == "transicoes":
                for transitions in values:
                    if not self.valid_transitions(key, transitions):
                        errors.append(key)
                break
            
            for validation in self.validate_type[key]:
                    if not validation(key, values):
                        errors.append(key)
                        
            if key in self.compositions and not errors:
                self.compositions[key].extend(values)

        return errors, set(self.compositions["alfabeto"])