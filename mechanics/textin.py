#!/usr/bin/env python

""" textin.py
    Creates a textbox wherever at specified coordinates.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/1/17
    python ver: 2.7
"""
import curses, curses.panel, curses.textpad, ConfigParser

c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("textin"):
    BORDER = c.getint("textin","border")
    TITLE_OFF = c.getint("textin","titleoff")
    BOX_OFF = c.getint("textin","boxoff")
    #DEFAULT_COLOR = c.getint("textin","defaultcolot")
else:
    BORDER = 1
    TITLE_OFF = 0
    BOX_OFF = 1
    DEFAULT_COLOR = 0

#Constants
DBORDER = BORDER * 2
BOX_DIFF = TITLE_OFF+BORDER+BOX_OFF 
TERMINATE = 7
KEY_ENTER = ord("\n")

def TextIn(text,y,x,h,w,color=0,exchar=KEY_ENTER):
    """ TextIn(text,y,x,h,w,color,exchar)
        Handles text input nicely
        
        y, x, h, w: Dimensions of the outer window.
        text: Header text
        color: Color of the window
        exchar: int of character used to return.
    """
    #Initialize backgound window
    curses.curs_set(1)
    if h < (DBORDER + TITLE_OFF + BOX_OFF + 1):
        h = DBORDER + TITLE_OFF + BOX_OFF + 1
    window = curses.newwin(h,w,y,x)
    window.attrset(curses.color_pair(color))
    window.bkgd(" ",curses.color_pair(color))
    window.border()
    window.addstr(BORDER,BORDER,text,
    curses.A_BOLD|curses.A_UNDERLINE|curses.color_pair(color))
    #Create textbox
    txtwin = window.subwin(h-(BOX_DIFF+1),w-DBORDER,y+BOX_DIFF,x+BORDER)
    text = curses.textpad.Textbox(txtwin)
    #Draw
    window.noutrefresh()
    txtwin.noutrefresh()
    curses.doupdate()
    #Checks if exit key is pressed
    def _validator(x):
        """Used to modify escape key, enter by default."""
        if x is exchar:
            x = TERMINATE
        return x
    del window
    return text.edit(_validator).strip()
             
#test code
if __name__ == "__main__":
    #init
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    curses.start_color()
    #test code
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_RED)
    test = TextIn("Enter exits",0,0,10,30,1,ord("\n"))
    stdscr.refresh()
    test = TextIn("Tab exits",4,25,4,30,1,ord("\t"))
    #reset
    curses.curs_set(1)
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
    print test
