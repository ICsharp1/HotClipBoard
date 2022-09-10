import clipboard
from asyncio.windows_events import NULL
#from curses import window
from tkinter import *
from tkinter import ttk
import pyautogui as pya
import tkinter
import time
# import clipboard_handler
# from clipboard_handler import clipF

from pynput.keyboard import Controller
keyboard = Controller()


hedict = {
    'q': '/',
    'a': 'ש',
    'z': 'ז',
    'w': '\'',
    's': 'ד',
    'x': 'ס',
    'e': 'ק',
    'd': 'ג',
    'c': 'ב',
    'r': 'ר',
    'f': 'כ',
    'v': 'ה',
    't': 'א',
    'g': 'ע',
    'b': 'נ',
    'y': 'ט',
    'h': 'י',
    'n': 'מ',
    'u': 'ו',
    'j': 'ח',
    'm': 'צ',
    'i': 'ן',
    'k': 'ל',
    ',': 'ת',
    'o': 'ם',
    'l': 'ך',
    '.': 'ץ',
    'p': 'פ',
    ';': 'ף',
    '/': '.',

    'Q': '/',
    'A': 'ש',
    'Z': 'ז',
    'W': '\'',
    'S': 'ד',
    'X': 'ס',
    'E': 'ק',
    'D': 'ג',
    'C': 'ב',
    'R': 'ר',
    'F': 'כ',
    'V': 'ה',
    'T': 'א',
    'G': 'ע',
    'B': 'נ',
    'Y': 'ט',
    'H': 'י',
    'N': 'מ',
    'U': 'ו',
    'J': 'ח',
    'M': 'צ',
    'I': 'ן',
    'K': 'ל',
    'O': 'ם',
    'L': 'ך',
    'P': 'פ',

    '/': 'q',
    'ש': 'a',
    'ז': 'z',
    '\\': 'w',
    'ד': 's',
    'ס': 'x',
    'ק': 'e',
    'ג': 'd',
    'ב': 'c',
    'ר': 'r',
    'כ': 'f',
    'ה': 'v',
    'א': 't',
    'ע': 'g',
    'נ': 'b',
    'ט': 'y',
    'י': 'h',
    'מ': 'n',
    'ו': 'u',
    'ח': 'j',
    'צ': 'm',
    'ן': 'i',
    'ל': 'k',
    'ת': ',',
    'ם': 'o',
    'ך': 'l',
    'ץ': '.',
    'פ': 'p',
    'ף': ';',
    '.': '/'
}


class clipF:
    def __init__(self):
        pass

    def get_selected_text(self):
        previous = clipboard.paste()
        pya.hotkey('ctrl', 'c')
        time.sleep(.01)
        selected = clipboard.paste()
        clipboard.copy(previous)
        return selected

    def hebrew_english(self, current_clipboard):

        fixed_clipboard = ''
        for i in current_clipboard:
            try:
                fixed_clipboard += hedict[i]
            except:
                continue

        return fixed_clipboard

    def fix_clipboard(self, window):
        selected_text = self.get_selected_text()
        fixed_clipboard = self.hebrew_english(selected_text)
        window.close_window()
        keyboard.type(fixed_clipboard)

    def print_fix(self):
        current_clipboard = clipboard.paste()
        fixed_clipboard = self.hebrew_english(current_clipboard)
        print(fixed_clipboard)


class MWindow:
    def __init__(self, gem="200x400+-5+200", resizablex=True, resizabley=True, cmd1=NULL):
        self.window = tkinter.Tk()
        self.window.title("You won't see it")
        self.window.geometry(gem)
        self.window.resizable(resizablex, resizabley)

        btn1 = tkinter.Button(self.window, text="Hebrew <==> English",
                              command=cmd1).grid(column=1, row=0)

    def close_window(self):
        self.window.destroy()

    def invisible(self):
        self.window.withdraw()

    def show(self):
        self.window.deiconify()

    def open(self):
        self.window.focus_force()
        self.window.focus
        self.window.mainloop()


def hebrew_english():
    print('not implemented')


clip = clipF()
window = MWindow(cmd1=lambda: clip.fix_clipboard(window))
window.open()
