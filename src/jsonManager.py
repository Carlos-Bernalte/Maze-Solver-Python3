#!/usr/bin/python3
# -- coding: utf-8 --

from tkinter import filedialog
import tkinter
import json, os
class jsonManager:
    def __init__(self):
        pass

    def read(self, file):
        with open(file, 'r') as output:
            data = json.load(output)
            output.close()
        return data

    def write(self, path, maze):
        with open(path, 'w') as output:
            if maze is not None: output.write(json.dumps(maze))
            output.close()
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