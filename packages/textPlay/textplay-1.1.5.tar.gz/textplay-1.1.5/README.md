<p align="center"><img src="https://raw.githubusercontent.com/rakeshkanna-rk/textPlay/main/textplay_logo.png" alt="TextPlay Logo" width="200"></p>

<br>

<H1 align="center">TextPlay</H1>

**Welcome to the TextPlay repository! 👋**  
This versatile Python module provides a range of text-related functions and tools to enhance your text analysis, summarization, translation, Morse code encoding/decoding, Google search, and more.

### To use my module

```bash
pip install textPlay
```

```python
import textPlay
```

## Features

### **🔍 Google Search:** This tool will search Google for a query and display the results. you can specify the number of results to display.

```python
from textPlay import google_search

search_query = "Python programming"
top_results = google_search(search_query, num_results=3)
print(top_results)
```

---

### **📣 Morse Code Encoder/Decoder:** This tool will encode and decode a message using the morse code. It will automatically detect if the input is morse code or text.

```python
from textPlay import morse

morse = Morse()

encoded_text = morse.coder("Hello, World!")
print("Encoded Text:", encoded_text)

decoded_text = morse.decoder(encoded_text)
print("Decoded Text:", decoded_text)
```

---

### **📦 Box:** This tool will print a box with a message and a title with specified length.

```python
from textPlay import box

title = "Title"
content = ["word 1", "word 2"]
width_percentage = 99  # Adjust as needed
box_with_title = create_box(title, content, width_percentage)
print(box_with_title)
```

---

### **🎨 Colors**: This tool will print text in different colors and styles.

```python
from textPlay import colors

print(f"{RED}This is red text{RESET}")
print(f"{BG_GREEN}This has a green background{RESET}")
print(f"{BOLD}This is bold text{RESET}")
```

---

### **📚 Options**: This tool will display a menu with options and handle user input for navigation and selection. Main function to display a menu with options and handle user input for navigation and selection.

```python
from textPlay import options

options(options=[('Option A', lambda: print("Option A selected")),
                ('Option B', lambda: print("Option B selected")),
                ('Option C', lambda: print("Option C selected")),
                ('Option D', lambda: print("Option D selected"))],
                index=">",
                head="Select an option:",
                delay=0.2,
                exit_msg="Exiting...")
```

---

### **🔑 Password Generator**: This tool will generate a random password with the specified length.

```python
from textPlay import password_generator

password = password_generator(length=12)
print(password)
```

---

### **🔐 Encryption Animation**: Simulate the encryption process by displaying random special characters before revealing the actual word.

```python
from textPlay import encrypt_animation

encrypted("Hello", sleep_time=0.1, end_color=BLUE, special_characters="!@#$%^&*()_+-=[]{}|;:,.<>?/")
```

---

### **🔃 Loader**: This tool will display a progress bar with a loading animation.

- **Progress Bar**: Simulate and display a progress bar incrementing from 0% to 100%.

```python
from textPlay import ProgressBar

if __name__ == "__main__":
    progress_bar = ProgressBar()
    try:
        progress_bar.start()
        time.sleep(3)  # Simulate a long-running task
    finally:
        progress_bar.stop()
```

- **Spinner**: Simulate and display a spinner animation.

```python
from textPlay import Spinner

if __name__ == "__main__":
    spinner = Spinner()
    try:
        spinner.start()
        time.sleep(3)  # Simulate a long-running task
    finally:
        spinner.stop()
```

- **Module Compiler**: Simulate and display a module compiling animation with active functioning.

```python
from textPlay import progressCompile

def func1(param1):
    time.sleep(1)  # Simulate processing
    print(f"\nProcessed with param1: {param1}")

def func2(param1, param2):
    time.sleep(2)  # Simulate processing
    print(f"\nProcessed with param1: {param1}, param2: {param2}")

def func3():
    time.sleep(1.5)  # Simulate processing
    print("\nProcessed with no params")


# Example usage with arguments
progressCompile(
    "Processing",
    ["Module A", "Module B", "Module C"],
    [func1, func2, func3],
    [(42,), ("Hello", "World"), ()]
)

# Example usage without arguments
progressCompile(
    "Processing",
    ["Module D", "Module E", "Module F"],
    [func3, func3, func3]
)
```

### **📁 Files**: This tool will list, delete, rename, and move files and folders.

```python
from textPlay import files

files = files.list_dir(USER)
print(files)
```

---

### **🛠️ Backend**: Executes the given command in the background using the subprocess module.

```python
from textPlay import backend

list_dir = backend.backend_exec("ls")
print(list_dir)
```

---

---

- **CLI**: A command line interface (CLI) for textPlay.

**Help**

```bash
textPlay --help
```

or

```bash
textPlay -h
```

To display all the CLI options

---

**Version**

```bash
textPlay --version
```

or

```bash
textPlay -v
```

To display the version of textPlay.

---

**Menu**

```bash
textPlay --menu
```

or

```bash
textPlay -m
```

To display the menu of textPlay.

---

**Contact**

```bash
textPlay --contact
```

or

```bash
textPlay -c
```

To display the contact details of textPlay.

---

**Update**

```bash
textPlay --update
```

or

```bash
textPlay -U
```

To update the textPlay module.

## Installation

To install the TextPlay module, you can download it directly by using `pip`

```bash
pip install textPlay
```

## Module Detials

- **VERSION:** `0.1.4`
- **TITLE:** `textPlay`
- **LICENSE:** `Apache License Version 2.0`
- **AUTHOR:** `Rakesh Kanna S`
- **AUTHOR EMAIL:** [rakeshkanna0108@gmail.com](mailto:rakeshkanna0108@gmail.com)
- **PYPI LIBRARY:** https://pypi.org/project/textPlay
- **GITHUB LIBRARY:** https://github.com/rakeshkanna-rk/textPlay
- **GITHUB PROFILE:** https://github.com/rakeshkanna-rk
