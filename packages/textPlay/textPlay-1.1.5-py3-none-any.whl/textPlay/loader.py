'''
# 1. Displays a loading progress bar in the terminal 
# 2. Displays a spinner animation in the terminal
# 3. Displays a compiled animation in the terminal 

'''

import sys
import os
from threading import Thread, Event
import threading
import time
import queue
import itertools

# ProgressBar class
class ProgressBar:
    """
    A class to display a progress bar in the terminal.

    Attributes:
        length (int): The total length of the progress bar.
        symbol (str): The symbol used for the completed portion of the bar.
        empty_symbol (str): The symbol used for the incomplete portion of the bar.
        color_on_completion (str): The color used when the bar reaches 100%.
    """

    def __init__(self, length=50, symbol="█", empty_symbol="-", color_on_completion="\033[92m"):
        """
        Initializes the ProgressBar object.

        Args:
            length (int): The total length of the progress bar. Default is 50.
            symbol (str): The symbol for the completed portion. Default is '█'.
            empty_symbol (str): The symbol for the incomplete portion. Default is '-'.
            color_on_completion (str): The color for the bar at 100% completion. Default is green.
        """
        self.length = length
        self.symbol = symbol
        self.empty_symbol = empty_symbol
        self.color_on_completion = color_on_completion
        self._stop_event = Event()

    def start(self):
        """
        Starts the progress bar simulation in a separate thread.
        """
        self._stop_event.clear()
        self._progress_thread = Thread(target=self._simulate_progress)
        self._progress_thread.start()

    def stop(self):
        """
        Stops the progress bar animation and ensures the terminal is ready for new lines.
        """
        self._stop_event.set()
        self._progress_thread.join()
        sys.stdout.write("\n")  # Move to a new line after the progress bar

    def _display(self, progress):
        """
        Displays the progress bar with the current progress value.

        Args:
            progress (float): The current progress as a float between 0 and 1.
        """
        filled_length = int(self.length * progress)
        bar = self.symbol * filled_length + self.empty_symbol * (self.length - filled_length)
        color = self.color_on_completion if progress == 1 else ''
        reset = "\033[0m"
        sys.stdout.write(f"\r|{color}{bar}{reset}| {progress:.1%}")
        sys.stdout.flush()

    def _simulate_progress(self):
        """
        Simulates a progress bar incrementing from 0% to 100%.
        """
        for i in range(101):
            if self._stop_event.is_set():
                break
            progress = i / 100
            self._display(progress)
            time.sleep(0.01)  # Simulate some processing time


# Spinner class
class Spinner:
    """
    A class to create a terminal spinner animation.

    Attributes:
        frames (list): The sequence of characters or symbols to display as spinner frames.
        interval (float): The time interval (in seconds) between frames.
        _stop_event (threading.Event): An internal event object to control the spinner's state.
    """

    def __init__(self, frames= None, interval:float=0.1):
        """
        Initializes the Spinner object.

        Args:
            frames (list, optional): A list of symbols to use as frames for the spinner animation.
                                     Defaults to a predefined list of braille-style symbols.
            interval (float, optional): Time interval in seconds between each frame. Defaults to 0.1 seconds.
        """
        self.frames = frames or ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.interval = interval
        self._stop_event = Event()

    def start(self):
        """
        Starts the spinner animation in a separate thread.
        """
        self._stop_event.clear()
        self._spinner_thread = Thread(target=self._spin)
        self._spinner_thread.start()

    def stop(self):
        """
        Stops the spinner animation and clears the spinner line in the console.
        """
        self._stop_event.set()
        self._spinner_thread.join()
        sys.stdout.write("\r")  # Clears the spinner line
        sys.stdout.flush()

    def _spin(self):
        """
        Private method that cycles through the spinner frames and displays them in the console.

        This method is run in a separate thread and stops when the `_stop_event` is set.
        """
        for frame in itertools.cycle(self.frames):
            if self._stop_event.is_set():
                break
            sys.stdout.write(f"\r{frame} ")
            sys.stdout.flush()
            time.sleep(self.interval)

# # Example usage
# if __name__ == "__main__":
#     spinner = Spinner()
#     try:
#         spinner.start()
#         # Simulate a long-running task
#         time.sleep(5)
#     finally:
#         spinner.stop()
#         print("Done!")

# if __name__ == "__main__":
#     progress_bar = ProgressBar()
#     try:
#         progress_bar.start()
#         time.sleep(3)  # Simulate a long-running task
#     finally:
#         progress_bar.stop()

import threading
import time
import queue
import itertools


def process_module(func, args, progress_queue, module_name):
    """
    Executes a given function in the background for a specific module.

    Args:
        func (callable): Function to process the module.
        args (tuple): Arguments to be passed to the function.
        progress_queue (queue.Queue): Queue to update progress.
        module_name (str): The name of the module being processed.
    """
    func(*args)  # Execute the function with the provided arguments
    progress_queue.put(module_name)


def spinner_animation(title, total_modules, progress_queue, stop_event):
    """
    Displays a dynamic loading spinner with real-time progress updates.

    Args:
        title (str): Title for the loading animation.
        total_modules (int): Total number of modules to process.
        progress_queue (queue.Queue): Queue to track progress updates.
        stop_event (threading.Event): Event to signal when the spinner should stop.
    """
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    completed = 0
    current_module = "Processing..."

    while not stop_event.is_set() or not progress_queue.empty():
        try:
            module_name = progress_queue.get_nowait()
            completed += 1
            current_module = module_name
        except queue.Empty:
            pass

        print(
            f"\r{title} {next(spinner)} ({completed}/{total_modules}) {current_module.ljust(30)}",
            end="",
            flush=True,
        )
        time.sleep(0.1)

    print(f"\r{title} ✓ ({total_modules}/{total_modules}) All Modules Processed{' ' * 30}")


def progressCompile(title, module_heads, func_list, func_args_list=None):
    """
    Manages the module processing and animation.

    Args:
        title (str): Title for the loader.
        module_heads (list): List of module names to process.
        func_list (list): List of functions to process the modules.
        func_args_list (list, optional): List of argument tuples for each function.

    Notes:
        - If the number of modules, functions, and arguments don't match, they are evenly distributed.
        - If func_args_list is None, it assumes all functions have no parameters.
    """
    total_modules = len(module_heads)
    total_functions = len(func_list)

    if total_functions != total_modules:
        func_list = (func_list * (total_modules // total_functions + 1))[:total_modules]

    if func_args_list is None:
        func_args_list = [()] * total_modules
    elif len(func_args_list) != total_modules:
        func_args_list = (func_args_list * (total_modules // len(func_args_list) + 1))[:total_modules]

    progress_queue = queue.Queue()
    stop_event = threading.Event()

    # Start module processing threads
    threads = []
    for module, func, args in zip(module_heads, func_list, func_args_list):
        thread = threading.Thread(target=process_module, args=(func, args, progress_queue, module))
        threads.append(thread)
        thread.start()

    # Start spinner animation in a separate thread
    spinner_thread = threading.Thread(
        target=spinner_animation,
        args=(title, total_modules, progress_queue, stop_event),
        daemon=True,
    )
    spinner_thread.start()

    # Wait for all processing threads to complete
    for thread in threads:
        thread.join()

    # Signal the spinner to stop
    stop_event.set()
    spinner_thread.join()


# Example functions
# def func1(param1):
#     time.sleep(1)  # Simulate processing
#     print(f"\nProcessed with param1: {param1}")

# def func2(param1, param2):
#     time.sleep(2)  # Simulate processing
#     print(f"\nProcessed with param1: {param1}, param2: {param2}")

# def func3():
#     time.sleep(1.5)  # Simulate processing
#     print("\nProcessed with no params")


# # Example usage with arguments
# progressCompile(
#     "Processing",
#     ["Module A", "Module B", "Module C"],
#     [func1, func2, func3],
#     [(42,), ("Hello", "World"), ()]
# )

# # Example usage without arguments
# progressCompile(
#     "Processing",
#     ["Module D", "Module E", "Module F"],
#     [func3, func3, func3]
# )

