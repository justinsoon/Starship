from tkinter import Tk  
from pynput import keyboard
from pynput.keyboard import Key, Controller

rawPaste = Controller()

def on_press(key):
    if key == Key.f4:
        content = Tk().clipboard_get()
        rawPaste.type(content)

print ('Raw Paste On!')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()