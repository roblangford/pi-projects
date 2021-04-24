# Simple Python Text input to output Morse code as a flashing led


#import gpiozero from led
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

# Declare length of the timings
dit_length = 0.25
dash_length = 0.75
space_length = 1.5

# function to get morse code from letter
def get_morse(morse, key):
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
    for morse_key in letter:
        if morse_key == ".":
            led.blink(on_time=dit_length,off_time=dit_length,n=1,background=False)
        if morse_key == "-":
            led.blink(on_time=dash_length,off_time=dit_length,n=1,background=False)
        if morse_key == "===":
            sleep(space_length)
    
def main():
    # Read User input
    userInput = input("Input Text:")

    # Iterate over input
    for ltr in userInput:
        morse_letter = get_morse(morse, ltr)
        led_morse(morse_letter)

if __name__ ==  "__main__":
    main()