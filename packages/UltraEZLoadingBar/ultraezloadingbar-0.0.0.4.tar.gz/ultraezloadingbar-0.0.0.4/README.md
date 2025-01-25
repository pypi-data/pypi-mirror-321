# UltraEZLoadingBar

`UltraEZLoadingBar` is a simple Python package that displays a loading bar in the console. 

## Installation
Install the package via pip:
pip install UltraEZLoadingBar

## loading_bar Function
loading_bar(steps, bar_length, delay_per_step, message, color)

Args:
    steps (int): Total number of steps (e.g., iterations).
    bar_length (int): The length of the loading bar in characters.
    delay_per_step (float): The delay between each step (in seconds).
    message (str): The prefix message before the loading bar.
    color (str): Optional. Adds color to the loading bar using ANSI escape codes. Examples: "r", "g", "b", etc.
    
    Usage:
        - Create A Loading Bar With 100 Steps And 100 Characters And 0.1 Second Delay And A Message Of "Loading... " And A Red Text Color
            Command: loading_bar(100, 100, 0.1, "Loading... ", "r")
        - Create A Loading Bar With 100 Steps And 100 Characters And 0.1 Second Delay And A Message Of "Processing... " And The Deafult Color
            Command: loading_bar(100, 100, 0.1, "Processing... ") (If You Want A Deafult Color Dont Add The Color Varible, If You Want No Text Put "" For The Varible)

## new_line Function
new_line()

Args:
    Creates a new line

    Usage
        - Create a new line
            Command: new_line()

## colored_text Function
colored_text(text, color)
Args:
    Prints the given text in the specified color.
    
    text (str): The text to be printed.
    color (str): The color of the text. Available colors: red, green, blue, etc.

    Usage:
        - Create Text With "Hello!" With a blue color
            Command: colored_text 


## Changelog (New!)
+ Changelog
+ New Line Function (Automatically Add A New Line) 
+ Colored Text Function (Color Your Text!)
