#!/usr/bin/env python

""" save.py
    A script to save and load files.
    
    Author: Jeremy Stintzcum
    Date last Modified: 10/28/17
    python ver: 2.7
"""

import pickle, os
import menu

#TODO move settings to file (ConfigParser)
HEIGHT = 7
WIDTH = 36
XPOS = 22
YPOS = 7
COLOR = 1
PATH = "./"

def save(clss, filename = "new", flext = ".gls"):
    """Saves a class to a file"""
    #check if file already exists
    if os.path.exists(PATH+filename+flext):
        selection = Menu(YPOS,XPOS,HEIGHT,WIDTH,COLOR,"This filename already exists.")
        selection.addItem("Continue", 0)
        selection.addItem("Discard", 1)
        choice = selection.run()
        if choice is 1:
            return
    f = open(filename+flext,"w+")
    pickle.dump(clss,f)
    f.close()

def load(filename, flext = ".gls")
    """Opens a file and returns a class"""
    if os.path.exists(PATH+filename+flext):
        f = open(PATH+filename+flext, "r")
        clss = pickle.load(f)
        f.close()
        return clss

#TODO set path, write to INI

#test code
if __name__ == "__main__":
    import curses
    #init
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    curses.start_color()
    #test code
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLUE)
    
    
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
