#!/usr/bin/python3
# -- coding: utf-8 --

import json, os

def read(file):
    with open(file, 'r') as output:
        data = json.load(output)
        output.close()
    return data

def write(maze):
    jsonFile= {"rows": maze.rows, "cols": maze.columns, "max_n": 4, "mov": [[-1, 0], [0, 1], [1, 0], [0, -1]], "id_mov": ["N", "E", "S", "O"], "cells": {}}
    for i in range(maze.rows):
        for j in range(maze.columns):
            jsonFile["cells"].update({"("+str(i)+", "+ str(j) +")": {"value": maze.grid[i][j].value, "neighbors": maze.grid[i][j].neighbours}})
        
    with open("mazes/Lab_"+str(maze.rows) + "_" + str(maze.columns) + ".json", "w") as file:
        json.dump(jsonFile, file, indent=4)

def writeProblem(initial, objective, maze, dimension):
    jsonFile={"INITIAL": "("+str(initial[0])+","+str(initial[1])+")", "OBJETIVE": "("+str(objective[0])+", "+str(objective[1])+")", "MAZE": maze}
    with open("problems/problem_"+str(dimension[0])+"x"+str(dimension[1])+".json", "w") as file:
        json.dump(jsonFile, file, indent=0)