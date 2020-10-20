#!/usr/bin/python3
# -- coding: utf-8 --

import json, os, Maze
class jsonManager:
    def __init__(self):
        pass

    def read(self, file):
        with open(file, 'r') as output:
            data = json.load(output)
            output.close()
        return data

    def write(self, maze):
        jsonFile= {"rows": maze.rows, "cols": maze.columns, "max_n": 4, "mov": [[-1, 0], [0, 1], [1, 0], [0, -1]], "id_mov": ["N", "E", "S", "O"], "cells": {}}
        for i in range(maze.rows):
            for j in range(maze.columns):
                print(i, " ", j)
                
                cell={"("+str(i)+", "+ str(j) +")": {"value": 0, "neighbors": maze.getMaze()[i][j].getNeighbours()}}
                
                jsonFile["cells"].update(cell)
        
        with open("results/Lab_"+str(maze.rows) + "_" + str(maze.columns) + ".json", "w") as file:
            json.dump(jsonFile, file, indent=4)