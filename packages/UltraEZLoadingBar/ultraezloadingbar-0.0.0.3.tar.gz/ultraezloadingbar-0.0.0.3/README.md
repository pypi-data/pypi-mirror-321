# UltraEZLoadingBar

`UltraEZLoadingBar` is a simple Python package that displays a loading bar in the console. 

## Installation
Install the package via pip:
pip install UltraEZLoadingBar

## Use
loading_bar(steps, bar_length, delay_per_step, message)

Args:
    steps (int): Total number of steps (e.g., iterations).
    bar_length (int): The length of the loading bar in characters.
    delay_per_step (float): The delay between each step (in seconds).
    message (str): The prefix message before the loading bar.
    color (str): Optional. Adds color to the loading bar using ANSI escape codes. Examples: "r", "g", "b", etc.