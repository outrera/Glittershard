#!/usr/bin/env python

""" configset.py
    This program automatically opens/creates an .ini file to write values.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/4/17
    python ver: 2.7
"""

import ConfigParser, curses
import textin, menu

#TODO Generic string setter
#TODO fix x,y,h,w

c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("configset"):
    STARTX = c.getint("configset","startx")
    STARTY = c.getint("configset","starty")
    TEXTBOXH = c.getint("configset","textboxh")
    TEXTBOXW = c.getint("configset","textboxw")
    DESCSTARTX = c.getint("configset","descstartx")
    DESCSTARTY = c.getint("configset","descstarty")
    DESCBOXH = c.getint("configset","descboxh")
    DESCBOXW = c.getint("configset","descboxw")
    DEFAULTCOLOR = c.getint("configset","defaultcolor")
else:
    STARTX = 25
    STARTY = 10
    TEXTBOXH = 4
    TEXTBOXW = 30
    DESCSTARTX = 10
    DESCSTARTY = 2
    DESCBOXH = 20
    DESCBOXW = 60
    DEFAULTCOLOR = 0
    
#Constants
TAB_KEY = ord("\t")

def getFloat(w,c,name,tag,text,color=DEFAULTCOLOR):
    """ getFloat(w,c,name,tag,text,color)
        Sets a float value
    
        w: menu to clear
        c: parser
        color: Color to use
        name: section
        tag: value
        text: display text
    """
    temp = textin.TextIn(text,STARTY,STARTX,TEXTBOXH,TEXTBOXW,color)
    try:
        temp = float(temp)
        "{0:.2g}".format(temp)
        temp = str(temp)
        c.set(name,tag,temp)
        w.window.touchwin()
        w.window.refresh()
    except:
        getFloat(w,c,name,tag,"Not a number:")
        
def getInt(w,c,name,tag,text,color=DEFAULTCOLOR):
    """ getInt(w,c,name,tag,text,color)
        Sets a int value
    
        w: menu to clear
        c: parser
        color: Color to use
        name: section
        tag: value
        text: display text
    """
    temp = textin.TextIn(text,STARTY,STARTX,TEXTBOXH,TEXTBOXW,color)
    try:
        int(temp)
        temp = str(temp)
        c.set(name,tag,temp)
        w.window.touchwin()
        w.window.refresh()
    except:
        getInt(w,c,name,tag,"Not an Integer:")

def getName(w,c,color=DEFAULTCOLOR):
    """ getName(w,c,color)
        Returns a string
    
        w: menu to clear
        c: parser
        color: Color to use
    """
    name = textin.TextIn("Enter a name:",STARTY,STARTX,0,TEXTBOXW,color)
    while c.has_section(name):
        name = textin.TextIn("Name already exists.",STARTY,STARTX,TEXTBOXH,
        TEXTBOXW,color)
    c.add_section(name)
    w.window.touchwin()
    w.window.refresh()
    return name
    
def getDesc(w,c,name,tag,color=DEFAULTCOLOR):
    """ getDesc(w,c,name,tag,color)
        Sets a description
    
        w: menu to clear
        c: parser
        color: Color to use
        name: section
        tag: value
    """
    temp = textin.TextIn("Description: (tab finishes)",DESCSTARTY,DESCSTARTX,
    DESCBOXH,DESCBOXW,TAB_KEY,color)
    c.set(name,tag,"\"" + temp + "\"")
    w.window.touchwin()
    w.window.refresh()

def getBool(w,c,name,tag,text,color=DEFAULTCOLOR):
    """ getBool(w,c,name,tag,text,color)
        Sets a boolean value
    
        w: menu to clear
        c: parser
        color: Color to use
        name: section
        tag: value
        text: display text
    """
    curses.curs_set(0)
    boolmenu = menu.Menu(STARTY,STARTX,TEXTBOXH,TEXTBOXW,text,color)
    boolmenu.addItem("True",1)
    boolmenu.addItem("False",2)
    selection = boolmenu.run()
    if selection is 1:
        c.set(name,tag,"true")
    else:
        c.set(name,tag,"false")
    w.window.touchwin()
    w.window.refresh()
