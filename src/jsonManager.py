#!/usr/bin/python3
# -- coding: utf-8 --

from tkinter import filedialog
import tkinter
import json, os
class jsonManager:
    #--Method to choose the file
    def select():
        root = tkinter.Tk()
        root.withdraw()

        path = filedialog.askopenfilename()
        return path

    #--Method to read any json file
    def read(): 
        path = jsonManager.select()
        #Falta try/except
        with open(path, 'r') as output:
            data = json.load(output)
            output.close()
        return data

    
    
