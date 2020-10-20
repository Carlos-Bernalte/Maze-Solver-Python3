# A1_11
This repository is destined to be the place of work for "Intelligent systems" class of Informatics Engineering  of UCLM 2020/2021

# Wilson's algorithm
Wilson’s algorithm uses loop-erased random walks to generate a uniform spanning tree — an unbiased sample of all possible spanning trees.<br>
The algorithm initializes the maze with an arbitrary starting cell. Then, a new cell is added to the maze, initiating a random walk (shown in magenta). The random walk continues until it reconnects with the existing maze (shown in white). However, if the random walk intersects itself, the resulting loop is erased before the random walk continues.
## Notes about the project
In order to execute this program you must have installed python3, and execute one of these two commands on your cmd or terminal<br>
  python3 -g ./main -g rows columns<br>
  python3 -f ./main -f file.json<br>
The first command will generate a random maze using the number of rows or columns you have selected and the second one will generate one from the json file you have selected
## Required libraries
These are the libraries we have used to write the code of: 
  - pygame
  - json
  - sys
  - random

## Classes
  - **main**:This is the main class of the project which makes everything work as intended
  - **jsonManager**:This class is used to read and write the .json files
  - **Maze**: This class possesses the logical part of the project
  - **Cell**: This class possesses the properties of the cells
## Methods
  - **Maze.generateRandomMaze(rows, columns)**<br>
  This method is used to generate a maze when choosing a randomize form 
  - **Maze.generateMazeJSON(JSON)**<br>
  This method is used to generate a maze when choosing the JSON form
  - **Maze.initLab()**<br>
  This method is used to initialize every cell as not visited and withoud neighbours
  - **Maze.checkMaze():boolean**<br>
  This method is used to assure that every cell in the grid has been visited, in case there is one or more not been visited it forces another iteration, in order to find every path
  - **Maze.chooseStartingCell()**<br>
  This method is used to select a cell which will be set to visited to assure that the algorithm can work. It is invoked by iterate()
  - **Maze.chooseRandomCell()**<br>
  This method is used to choose a random cell which the path will start with. It is invoked by iterate()
  - **Maze.randomizeDir()**<br>
  This method is used to generate a random direction in which the maze must go. This method is called by the method generateLab()
  - **Maze.deleteLoop()**<br>
  This method checks whether a cell has been visited on the current path, which would cause a loop, an in that case it restores every cell untill is comes to the last one, which have caused the loop. This method is invoked by the method generateLab()
  - **Maze.generateLab()**<br>
  This method creates a "path" which will be filled with the frontier cells. After that it will generate the path by using randomizeDir() and deleteLoop() to make sure it gets to the destination randomly and avoiding loops
  - **Maze.iterate()**<br>
  This method starts the work of the algorithm and invokes methods chooseStartingCell(),chooseRandomCell() and generateLab
  - **main.parse_argv():int**<br>
  This method parses the argument you have to select on the command line
  - **main.drawMaze(my_maze)**<br>
  This method drows the maze into an image
  - **jasonManage.read(path):data**<br>
  This method is used to read the json

## OUTPUT
  - json
  - image.png
  
