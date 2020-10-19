import json
class jsonManager:
    #grid[]

    def __init__(self):
        with open("C:\\Users\\ANGEL\\Desktop\\cosas de programar\\repositorios VS\\A1_11\\jsonImput\\puzzle_10x20.json") as f: 
            data=json.load(f)
        self.nrows=data['rows']
        self.ncols=data['cols']
        self.max_n=data['max_n']
        self.mov=data['mov']
        self.id_mov=data['id_mov']
        #for c in data['cells']:

    def writeJson(self):
        
    
    def get_nrows(self):
        return self.nrows
    def get_ncols(self):
        return self.ncols
    