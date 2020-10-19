#!/usr/bin/python3
# -- coding: utf-8 --

from tkinter import filedialog
import tkinter
import json, os
class jsonManager:

    #--Metodo para leer el hijo de Jay

    def read(self, path): 
        with open(path, 'r') as output:
            data = json.load(output)
            output.close()
        return data


    
    
