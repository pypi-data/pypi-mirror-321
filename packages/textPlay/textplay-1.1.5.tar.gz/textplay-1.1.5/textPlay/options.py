"""
# Options

This module provides a function to display a menu with options and handle user input for navigation and selection.

Functions:
    - options(options: list, index: str = ">", head: str = "", delay: float = 0.1, exit_msg: str = "Exiting...", exit_key: str = "esc")

Example:
if __name__ == "__main__":
    options(
        options=[
            ('Option A', lambda: print("Option A selected")),
            ('Option B', lambda: print("Option B selected")),
            ('Option C', lambda: print("Option C selected")),
        ],
        index=">",
        head="Select an option:",
        delay=0.1,
        exit_msg="Goodbye!"
    )
    
"""
import os
import time
import sys
from typing import Callable, List, Tuple

def print_options(selected_index, options, index, head, helper):
    """
    Print options with highlighting for the selected option.

    Args:
        selected_index (int): Index of the currently selected option.
        options (list of tuples): List of options, each with a name and associated function.
        index (str): Indicator for the selected option.
        head (str): Heading displayed above the options.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    if head:
        print(head)
    if helper:
        print("Use 'up' and 'down' to navigate, 'enter' to select, and 'esc' to exit.")
    for i, (option_name, _) in enumerate(options):
        if i == selected_index:
            print(f"{index} {option_name}")  # Highlight selected option
        else:
            print(f"  {option_name}")  # Normal option


def options(
        options: List[Tuple[str, Callable]], 
        index: str=">", 
        head: str = "", 
        delay: float=0.1, 
        exit_msg: str="Exiting...", 
        helper: bool = True,
        ):
    """
    Display a menu with options and handle user input for navigation and selection.

    Args:
        - options (list of tuples): List of options, each with a name and associated function.
        - index (str, optional): Indicator for the selected option. Default is '>'.
        - head (str, optional): Heading displayed above the options. Default is an empty string.
        - delay (float, optional): Delay in seconds between option navigation. Default is 0.1.
        - exit_msg (str, optional): Message displayed when exiting. Default is "Exiting...".
        - exit_key (str, optional): Key to exit the program. Default is 'esc'.

    Example:
        options(options=[
            ('Option A', lambda: print("Option A selected")),
            ('Option B', lambda: print("Option B selected")),
            ('Option C', lambda: print("Option C selected")),
        ])
    """
    if os.name == 'nt':  # Windows
        import msvcrt

        def get_key():
            key = msvcrt.getch()
            if key in (b'\x00', b'\xe0'):  # Arrow keys are preceded by null byte
                key += msvcrt.getch()
            return key

        KEY_UP = b'\xe0H'
        KEY_DOWN = b'\xe0P'
        KEY_ENTER = b'\r'
        KEY_ESC = b'\x1b'

    else:  # Unix-like
        import termios
        import tty

        def get_key():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return key

        KEY_UP = '\x1b[A'
        KEY_DOWN = '\x1b[B'
        KEY_ENTER = '\r'
        KEY_ESC = '\x1b'

    selected_index = 0
    while True:
        print_options(selected_index, options, index, head, helper)
        key = get_key()

        if key == KEY_ESC:  # ESC key
            print(exit_msg)
            break
        elif key == KEY_ENTER:  # Enter key
            options[selected_index][1]()  # Execute associated function
            break
        elif key == KEY_UP:  # Up arrow
            selected_index = (selected_index - 1) % len(options)
            time.sleep(delay)
        elif key == KEY_DOWN:  # Down arrow
            selected_index = (selected_index + 1) % len(options)
            time.sleep(delay)


# if __name__ == "__main__":
#     options(
#         options=[
#             ('Option A', lambda: print("Option A selected")),
#             ('Option B', lambda: print("Option B selected")),
#             ('Option C', lambda: print("Option C selected")),
#         ],
#         index=">",
#         head="Select an option:",
#         delay=0.1,
#         exit_msg="Goodbye!"
#     )
