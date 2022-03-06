# Morse Code

Code: Python

---
## Description
Project started out as a simple encoder to convert text input to morse code strings.

---
## Declaration
```python
#import LED function from gpiozero module: https://github.com/gpiozero/gpiozero
from gpiozero import LED
#import sleep for timings
from time import sleep
```

---
## Process
Simple string input is then iterated over a letter at a time, an if statement is used to check against the keys in the morse dictionary and returns the value.
The returned value from the morse code string is then sent to the pi project board.
