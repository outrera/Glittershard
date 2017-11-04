#!/usr/bin/env python

""" savehandler.py
    A script to save and load files.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/4/17
    python ver: 2.7
"""

import pickle, os
import menu, 

#TODO Make path editor

c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("save")
    WIDTH = c.getint("save","width")
    HEIGHT = c.getint("save","height")
    STARTX = c.getint("save","startx")
    STARTY = c.getint("save","starty")
    PATH = c.get("save","path")
else:
    HEIGHT = 7
    WIDTH = 36
    STARTX = 22
    STARTY = 7
    PATH = "./"

def Save(clss, filename = "new", flext = ".gls", color=0):
    """Saves a class to a file"""
    #check if file already exists
    if os.path.exists(PATH+filename+flext):
        selection = menu.Menu(STARTY,STARTX,HEIGHT,WIDTH,COLOR,
        "This filename already exists.")
        selection.addItem("Continue", 0)
        selection.addItem("Discard", 1)
        choice = selection.run()
        if choice is 1:
            return
    f = open(filename+flext,"wb+")
    pickle.dump(clss,f)
    f.close()

def Load(filename, flext = ".gls")
    """Opens a file and returns a class"""
    if os.path.exists(PATH+filename+flext):
        f = open(PATH+filename+flext, "rb")
        clss = pickle.load(f)
        f.close()
        return clss
        
def Path:
    """Changes the save path to save and load files to"""
    pass
