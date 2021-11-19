import re

from traitlets.traitlets import validate

class EntryValidator:
    
    def valid_types():
        
        types = {
            "alphabet": r'^[a-z]$',
            "states": r'^q[0-9]+$',
            "empty": [],
            "lenght": 1,
        }
        
        validate_type = {
            
            "alfabeto": [types["alphabet"], types["empty"]],
            "estados": [types["states"], types["empty"]],
            "inicial": [types["states"], types["empty"], types["lenght"]],
            "final": [types["states"]],
            
        }
        
    # def validator_with_tag(data=dict):
        
        # for key,values in data.items():
            
        #     for value in values:
                
            
            
            
            
        
        
        
        
    
        