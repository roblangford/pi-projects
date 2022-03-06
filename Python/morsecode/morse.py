# Simple Python Text input to output Morse code as a flashing led


#import gpiozero from led
import sys
from gpiozero import LED
from time import sleep

#Set the LED pin according to BCM numbering
led = LED(17)

# Dictionary of letter to morse
morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "..-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

# Declare length of the timings for led blinks in seconds
dit_length = 0.25
dash_length = 0.75
space_length = 1.5

# function to get morse code from letter
def get_morse(morse, key):
    """
    Converts input letters to morse code using the morse dictionary, if the space character is detected the string "===" is returned.


    Args:
        morse: passes the morse dictionary.
        key: letter to be converted.

    Returns:
        function will either return the morse key for the input character or the === to denote a space.
    """
    key = key.lower()
    if key in morse.keys():
        print(key +" = "+ morse[key])
        return morse[key]
    else:
        if key == " ":
            print("space")
            return "==="

# function to convert morse 'dot' and 'dash' into LED output
def led_morse(letter):
    """
    Simple function to iterate the morse key input and uses led.blink function to output on a raspberry pi project board via GPIO.
    
    Args: 
        letter: string represents the morse key character as dots '.'  dashes '-'
    """
    for morse_key in letter:
        if morse_key == ".":
            led.blink(on_time=dit_length,off_time=dit_length,n=1,background=False)
        if morse_key == "-":
            led.blink(on_time=dash_length,off_time=dit_length,n=1,background=False)
        if morse_key == "===":
            sleep(space_length)
    
def main(userInput):
    """
    Program converts a string of text input to morse code and then outputs via an led on a raspberry pi project board via GPIO.
    See README on repo for details on the hardware used.

    """
    # Iterate over input
    for ltr in userInput:
        morse_letter = get_morse(morse, ltr)
        led_morse(morse_letter)

if __name__ ==  "__main__":
    try:
        # checks for 1st input argument and assigns value to userInput
        userInput = sys.argv[1]
    except IndexError:
        # prompts for user input if no argument string passed from cli
        userInput = input("Input Text: ")
    main(userInput)