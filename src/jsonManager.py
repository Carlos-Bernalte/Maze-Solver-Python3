#!/usr/bin/python3
# -- coding: utf-8 --

from tkinter import filedialog
import tkinter
import json, os
class jsonManager:

    #--Metodo para leer el hijo de Jay

    def read(path):
        try:
            with open(path, 'r') as output:
                data = json.load(output)
                output.close()
        except:
            print("Reading ERROR! The typed file does not exist.")
        return data

    '''
    def write(name, maze):
        structure = 
        {
            "rows": ,
            "cols": ,
            "max_n": ,
            "mov": [[-1, 0], [0, 1], [1, 0], [0, -1]]
            "id_mov": ["N", "E", "S", "O"]
            "cells": 
            {
                "()"
            }
        }
        '''