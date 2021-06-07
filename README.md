# A1_11
This repository is destined to be the place of work for **"Intelligent Systems"** class of Computer Engineering in UCLM 2020/2021


## Notes about the project
In order to execute this program you must have installed python3 and execute the program with: <br>
```sh
$python .\src\Main.py  
````
Once you execute the program you must see an option menu like: <br>
```sh
##### Choose what you want to do: #####
 •(0) Exit.
 •(1) Generate a random maze.
 •(2) Create a maze from JSON.
 •(3) Test insertion on frontier
 •(4) Define a problem.
>ANSWER:
 ```
 Then, if you choose optio zero, the program will end<br>
 If you choose option number one, our program create a Maze with a random size and save the solution in .json format and an image in .png format.<br>
 If you select option number two, a new window runs in your PC in order to select the file you want to execute with our program from a selected .json.<br>
 If you choose option number three, it will test manually the correct insertion of diferent nodes in the Frontier, create diferent nodes (i,j) with diferent values each other to prove the complete execution of our program.<br>
 Finally, choosing option four, you can change the initial and objetive cell of a maze to make a new problem<br>
 
 
The first command will generate a random maze using the number of rows or columns you have selected and the second one will generate one from the json file you have selected
## Required libraries
These are the libraries we have used to write the code of: 
```sh
  - Pillow
  - Json
  - sys
  - random
  - os
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
  - **Frontier**: The frontier class offer to the search a data structure which can be ordered depending on some value.
  - **Node**: This class contains all the properties of each node created by the agent program and a toString() which return us all the information of a Node.
  - **SpeedTest**: The purpose of this class is to explain which data structure we have selected. As Python groups lists, stacks and queues on the list type we cannot test them independently, in its place Python offers us sets, dictionaries and tuples. As dictionaries need a key for each entry, we are not going to test them. Tuples are the slowest of the remaining three, apart from the fact that you cannot remove any item, you can only group them. The difference between sets and lists is that both are very fast introducing new elements, and when there are few elements to be introduced sets are actually faster than lists, but when you introduce more elements sets start introducing them slower than lists.
  - **Drawer**: The purpose of this class is to draw the resulting maze developed with the agent program and it is used to draw the solution of a maze problem.
  - **Problem**: This class is used to allocate the initial and obetive positions  and which strategy you are following a part from getting whether a state is the goal or not
  - **searchSolution**: this file contains every necessary method related to reaching the goal according to the strategy selected

## Output
```sh
  - json
  - image.png
```
