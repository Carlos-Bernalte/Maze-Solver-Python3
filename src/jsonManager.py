#!/usr/bin/python3
# -- coding: utf-8 --

from tkinter import filedialog
import tkinter
import json, os
class jsonManager:

<<<<<<< HEAD
    #--Method to read any json file
    def read(): 
        path = jsonManager.select()
        #Falta try/except
=======
    #--Metodo para leer el hijo de Jay

    def read(self, path): 
>>>>>>> ada2f9009888012e26934ca008286823f023a567
        with open(path, 'r') as output:
            data = json.load(output)
            output.close()
        return data


    
    
