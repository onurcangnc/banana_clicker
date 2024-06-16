import pyautogui
import time
from pynput import keyboard
from PIL import Image

# Load the image to be clicked
image_path = "banana.png"

# Flags to control the clicking
clicking = True
paused = False

# Set pyautogui pause time to a very small value for faster clicking
pyautogui.PAUSE = 0.00001

'''
you can adjust the speed of the clicking by 
modifying both .PAUSE method & time.sleep() method
Thanks for watching ! ! !
'''

# Function to be called when a key is pressed
def on_press(key):
    global clicking, paused
    try:
        if key.char == 'p':
            paused = True
            print("Paused")
        elif key.char == 'c':
            paused = False
            print("Continued")
        elif key == keyboard.Key.esc:
            clicking = False
            return False
    except AttributeError:
        pass

# Locate the image on the screen
location = None
while location is None:
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        pass
    time.sleep(0.1)

if location is None:
    print("Image not found on the screen.")
    exit()

# Start the listener for the keyboard keys
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Click very fast on the image
try:
    while clicking:
        if not paused:
            pyautogui.click(location)
except KeyboardInterrupt:
    pass

# Wait for the listener to stop
listener.join()

print("Script stopped.")
