import sys
import time

def loading_bar(steps, bar_length, delay_per_step):
    """
    Displays a default color text loading bar in the console.
    
    Args:
        steps (int): Total number of steps (e.g., iterations).
        bar_length (int): The length of the loading bar in characters.
        delay_per_step (float): The delay between each step (in seconds).
    """
    for current_step in range(steps + 1):
        # Calculate progress
        filled_length = int((current_step / steps) * bar_length)
        bar = "[" + "=" * filled_length + " " * (bar_length - filled_length) + "]"
        # Print the bar on the same line
        sys.stdout.write(f"\r{bar} {current_step}/{steps}")
        sys.stdout.flush()
        time.sleep(delay_per_step)  # Simulate work
