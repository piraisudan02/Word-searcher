![Screenshot 2024-02-20 234807](https://github.com/piraisudan02/Word-searcher/assets/96645021/94caea0c-01a0-4c5b-9eaf-d437cad29470)
![Screenshot 2024-02-20 235206](https://github.com/piraisudan02/Word-searcher/assets/96645021/e5e1da35-498e-44a9-a5c4-dbed6c3285ad)
![Screenshot 2024-02-20 235246](https://github.com/piraisudan02/Word-searcher/assets/96645021/228c4e68-a6b5-40ff-b16e-c002e8cfc609)
![Screenshot 2024-02-20 235322](https://github.com/piraisudan02/Word-searcher/assets/96645021/7c0a93ea-4bc9-4c2f-a839-8fdb7f3461df)
![Screenshot 2024-02-20 235610](https://github.com/piraisudan02/Word-searcher/assets/96645021/33a94b6c-e2ae-431c-8c2a-ab4eba1119fb)
![Screenshot 2024-02-20 235703](https://github.com/piraisudan02/Word-searcher/assets/96645021/b0df8088-04df-4db1-a2f9-cccd182d40f3)
![Screenshot 2024-02-20 235743](https://github.com/piraisudan02/Word-searcher/assets/96645021/01405e78-14f3-4e0b-9d17-bddc0b9ab845)
![Screenshot 2024-02-20 235808](https://github.com/piraisudan02/Word-searcher/assets/96645021/b34c04da-fa4c-4424-95a7-c7c4a6cd472a)
# Word-searcher
Imports:

The script imports necessary modules such as tkinter for GUI creation and messagebox for displaying messages.
Tkinter Setup:

A Tkinter window named "Word Search Game" is created.
Labels and entry widgets are used to prompt the user to enter the number of rows and columns for the word search grid.
Solution Class:

The Solution class contains a method named exist, which searches for a given word in a 2D board (grid) of characters. This class uses a recursive depth-first search (DFS) approach to find the word.
Grid Creation and Validation:

Functions are defined to create the word search grid based on the user's input for the number of rows and columns.
Validation functions ensure that the user inputs valid row and column values.
Word Search Functionality:

The search_word function is triggered when the user clicks the "Create Grid" button.
It validates the grid dimensions and the entered word.
It then searches for the word in the grid using the exist method from the Solution class.
If the word is found, a message box displays a success message along with the path of the word in the grid. If not found, it displays a message indicating the absence of the word.
GUI Layout:

The GUI elements are organized using labels, entry widgets, and buttons to create a user-friendly interface for the word search game setup.
Main Loop:

The Tkinter event loop (mainloop()) is started to run the GUI application, allowing users to interact with the interface.
