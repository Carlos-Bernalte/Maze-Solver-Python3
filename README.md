# A1_11
This repository is destined to be the place of work for **"Intelligent Systems"** class of Computer Engineering in UCLM 2020/2021

# Wilson's Algorithm
**Wilson’s Algorithm** uses loop-erased random walks to generate a uniform spanning tree — an unbiased sample of all possible spanning trees.<br>
The algorithm initializes the maze with an arbitrary starting cell. Then, a new cell is added to the maze, initiating a random walk (shown in magenta). The random walk continues until it reconnects with the existing maze (shown in white). However, if the random walk intersects itself, the resulting loop is erased before the random walk continues.

## Notes about the project
In order to execute this program you must have installed python3.<br>
Once you execute the program you must see an option menu like: <br>
```sh
##### Choose what you want to do: #####
 •(1) Generate a random maze.
 •(2) Create a maze from JSON.
 •(3)Test insertion on frontier
>ANSWER:
 ```
 Then, if you choose the first option, our program create a Maze with a random size and save the solution in .json format and an image in .png format.<br>
 If you select the second option, a new window runs in your PC in order to select the file you want to execute with our program from a selected .json.<br>
 Finally, the last option test manually the correct insertion of diferent nodes in the Frontier, we create diferent nodes (i,j) with diferent values each other to prove<br> the correct execution of our program.
 
The first command will generate a random maze using the number of rows or columns you have selected and the second one will generate one from the json file you have selected
## Required libraries
These are the libraries we have used to write the code of: 
```sh
  - Pillow
  - Json
  - sys
  - random
  - Tkinter
```
**You can install all of the external libraries with:** <br>

```sh
 pip install -r requirements.txt
```
In this document .txt you can find all the commands to install the required libraries but you can install all of them with the above command.

## Classes
  - **Main**:This is the main class of the project which makes everything work as intended
  - **JsonManager**:This class is used to read and write the .json files
  - **Maze**: This class possesses the logical part of the project
  - **Cell**: This class possesses the properties of the cells
  - **Frontier**: The purpose of this class is manage the implementation of the Frotier.
  - **Node**: This class already has the properties of the nodes.
  - **SpeedTest**: The purpose of this class is to explain which data structure we have selected. As Python groups lists, stacks and queues on the list type we cannot test them independently, in its place Python offers us sets, dictionaries and tuples. As dictionaries need a key for each entry, we are not going to test them. Tuples are the slowest of the remaining three, apart from the fact that you cannot remove any item, you can only group them. The difference between sets and lists is that both are very fast introducing new elements, and when there are few elements to be introduced sets are actually faster than lists, but when you introduce more elements sets start introducing them slower than lists.
  -**Drawer**: The purpose of this class is to draw the maze and in the future, to draw the path using the selected strategy.
  -**Functions**: This class contains the algorithm to create the Successor Function of the Maze executed.

## Output
```sh
  - json
  - image.png
```

