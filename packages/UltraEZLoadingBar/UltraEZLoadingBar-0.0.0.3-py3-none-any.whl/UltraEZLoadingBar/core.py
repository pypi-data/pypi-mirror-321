import sys
import time

def loading_bar(steps=50, bar_length=50, delay_per_step=0.1, message="Loading... ", color=None):
    """
    Displays a horizontal loading bar in the console.

    Args:
        steps (int): Total number of steps.
        bar_length (int): The length of the loading bar in characters.
        delay_per_step (float): The delay between each step (in seconds).
        message (str): The message to display before the loading bar.
        color (str): Optional. Adds color to the loading bar using ANSI escape codes. Examples: "r", "g", "b", etc.
    """
    # Define basic ANSI color codes
    colors = {
        "r": "\033[91m",
        "g": "\033[92m",
        "y": "\033[93m",
        "b": "\033[94m",
        "m": "\033[95m",
        "c": "\033[96m",
        "w": "\033[97m",
        "refresh": "\033[0m"
    }
    
    # Apply color if specified
    start_color = colors.get(color, "")  # Get the color code or empty string if invalid
    reset_color = colors["refresh"]

    for current_step in range(steps + 1):
        # Calculate progress
        filled_length = int((current_step / steps) * bar_length)
        bar = f"[{'=' * filled_length}{' ' * (bar_length - filled_length)}]"
        
        # Print the bar on the same line without adding extra lines
        sys.stdout.write(f"\r{start_color}{message}{bar} {current_step}/{steps}{reset_color}")
        sys.stdout.flush()
        time.sleep(delay_per_step)

    # Clear and overwrite the bar with a "Complete!" message
    sys.stdout.write("\n")
