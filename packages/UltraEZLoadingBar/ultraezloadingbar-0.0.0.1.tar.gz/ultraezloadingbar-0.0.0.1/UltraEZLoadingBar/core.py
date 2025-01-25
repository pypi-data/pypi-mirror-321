import sys
import time

def loading_bar(steps, bar_length, delay_per_step, message):
    """
    Displays a default color text loading bar in the console.
    
    Args:
        steps (int): Total number of steps (e.g., iterations).
        bar_length (int): The length of the loading bar in characters.
        delay_per_step (float): The delay between each step (in seconds).
        message (str): The prefix message before the loading bar.
    """
    try:
        # Initialize the loading bar (just the empty space part, with the message)
        bar_template = message + "[" + " " * bar_length + "]"

        # Iterate through steps
        for current_step in range(steps + 1):
            # Calculate progress (how much of the bar is filled)
            filled_length = int((current_step / steps) * bar_length)
            # Construct the bar with the filled part and the remaining empty part
            bar = bar_template[:len(message)] + "[" + "=" * filled_length + " " * (bar_length - filled_length) + "]"
            
            # Print the loading bar, overwrite the previous one on the same line
            sys.stdout.write(f"\r{bar} {current_step}/{steps}")
            sys.stdout.flush()  # Make sure the progress bar updates immediately
            time.sleep(delay_per_step)  # Simulate some work

        # After completion, print a final newline to ensure the next output starts from a new line
        print()

    except Exception as e:
        # Handle any errors and print the exception message
        print(f"An error occurred: {e}")
        sys.exit(1)