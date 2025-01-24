# Python text menu
Python module for interacting with the user through console, to install module from pip execute:
```bash
pip install python_text_menu
```

## Simple use
```python
from python_text_menu import print_menu, ask_option

options = ['Option 1', 'Option 2', 'Option 3']
print_menu(options)
choice = ask_option(len(options))
```
Output:
```
Menu:
[1] Option 1
[2] Option 2
[3] Option 3
[4] Exit
Select an option: 
```

Then you can create your own flow based on 'choice':
```
if choice == '1':
    # Do something
elif choice == '2':
    # Do something else
...
```

> [!WARNING] 
> Consider that ask_option() implements the built-in input() function and as such it locks the code flow

## Customize

You can customize it by giving it a title, a separator and/or an input text:


```python
options = ['Option 1', 'Option 2', 'Option 3']
choice = print_menu(options, title='New title', sep=''*20, input_text='Choose something...')
```
Output:
```
New title:
====================
[1] Option 1
[2] Option 2
[3] Option 3
[4] Exit
Choose something...
```
