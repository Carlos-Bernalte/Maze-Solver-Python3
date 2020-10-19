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

    #--Metodo para leer el hijo de Jay
    def read(): 
        path = jsonManager.select()
        with open(path, 'r') as output:
            data = json.load(output)
            output.close()
        return data
    
