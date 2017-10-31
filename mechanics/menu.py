#!/usr/bin/env python

""" menu.py
    menu class for creating menus
    
    Desc: Supports creation of menu and menu items before the menu is called, 
    and can be modified at any time
    Author: Jeremy Stintzcum
    Date last Modified: 10/31/17
    python ver: 2.7
"""
import curses, curses.panel
EXIT = -1 #exit condition
KEY_ESC = 27
KEY_ENTER = 10
RUNNING = -2 #While loop condition

#TODO Move settings to file
#settings
BORDER = 1 #size of border
CURSOR = "-=>" #cursor
CURSOR_CLR = "   " #same length as cursor
CURSOR_STARTPOS = 2 #starting x position of cursor
ITEM_OFF = len(CURSOR) + CURSOR_STARTPOS + BORDER #listed item offset
LINE_OFF = 2 #standard offset
NEXT = "Next Page"
TEXT_OFF = 0 #Space between title and first entry
TITLE_OFF = 0

class Menu:
    """ Menu(y, x, h, w, color, title)
        Creates a menu with the given parameters
        
        y: y offset
        x: x offset
        h: horizontal height
        v: vertical width
        color: the color the menu will appear as
        title: Title text
    """
    def __init__(self,y,x,h,w,color=0,title=""):
        #init vars
        self.select = 0
        self.y = y
        self.x = x
        self.h = h
        self.w = w
        self.items = []
        self.page = 1
        self.color = color
        self.title = title
        self.maxlistsize = (self.h-(2*BORDER+TEXT_OFF+TITLE_OFF))/LINE_OFF
        self.maxpage = 1
        #create window and set attributes
        self.window = curses.newwin(self.h,self.w,self.y,self.x)
        self.window.keypad(1)
        self.window.attrset(curses.color_pair(self.color))
        self.window.bkgd(" ",curses.color_pair(self.color))
        self.window.border()
        self.window.addstr((self.select*LINE_OFF)+LINE_OFF,CURSOR_STARTPOS,
        CURSOR)
        self.window.addstr(BORDER+TITLE_OFF, BORDER, self.title, 
        curses.A_BOLD|curses.A_UNDERLINE|curses.color_pair(self.color))
        self.update()
        #set panel
        self.panel = curses.panel.new_panel(self.window)

    def run(self):
        """ run()
            Executes the menu, getting input and returning a integer to select a
            function. Returns an integer used to branch in an if-else loop
        """
        self.update()
        state = RUNNING
        while state is RUNNING:
            key = self.window.getch()
            if key == KEY_ESC:
                state = EXIT
            elif key == curses.KEY_UP: #up
                self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
                CURSOR_STARTPOS,CURSOR_CLR)
                self.select = self.select - 1
                if self.select < 0:
                    self.select = self.maxlistsize-1
                    if len(self.items) < self.select:
                        self.select = len(self.items)-1
                self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
                CURSOR_STARTPOS,CURSOR)
            elif key == curses.KEY_DOWN: #down
                self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
                CURSOR_STARTPOS,CURSOR_CLR)
                self.select = self.select + 1
                if (self.select > self.maxlistsize-1 or 
                self.select > len(self.items)-1):
                    self.select = 0
                self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
                CURSOR_STARTPOS,CURSOR)
            elif key == KEY_ENTER:
                state = self.select
                if (state is self.maxlistsize-1 and
                len(self.items) > self.maxlistsize):
                    self.page = self.page + 1
                    if self.page > self.maxpage:
                        self.page = 0
                    state = RUNNING
                    self.update()
                elif state+(self.page*self.maxlistsize-1) < len(self.items):
                    return self.items[state+(self.page*self.maxlistsize-1)][1]
                else:
                    state = RUNNING
                    self.select = 0
                    self.update()
                    
            
    def update(self):
        """Updates window"""
        self.window.clear()
        self.window.border()
        self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
        CURSOR_STARTPOS,CURSOR)
        self.window.addstr(BORDER,BORDER,str(self.page),curses.A_BOLD|
        curses.A_UNDERLINE|curses.color_pair(self.color))
        if len(self.items) <= self.maxlistsize:
            for i in range(len(self.items)):
                self.window.addstr((LINE_OFF*i)+LINE_OFF,ITEM_OFF,
                self.items[i][0])
        else:
            for i in range(self.maxlistsize-1):
                if i+(self.maxlistsize-1)*self.page < len(self.items):
                    self.window.addstr((LINE_OFF*i)+LINE_OFF,ITEM_OFF,
                    self.items[i+(self.maxlistsize-1)*self.page][0])
            self.window.addstr((LINE_OFF*self.maxlistsize),
            ITEM_OFF,NEXT)
            
    def addItem(self,name,com=0):
        """ addItem(name,command)
            Adds a new item to the menu and refreshes panels
            
            name: the displayed string
            command: int value to be returned on selection
        """
        name = "{message: <{width}}".format(message=name, 
        width=self.w-ITEM_OFF-2)
        tup = (name,com)
        self.items.append(tup)
        #if self.maxlistsize < len(self.items):
         #   self.maxpage
    
    def rmItem(self, command):
        """ rmItem(command)
            Removes an item from the menu and refreshes panels
            
            command: the int value of the "command" attribute of the dict
        """
        self.select = 0
        for i in range(len(self.items)-1):
            if self.items[i][1] is command:
                self.items.pop(i)
    
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
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)
    testmenu = Menu(1,1,10,60,1,"Test")
    testmenu.addItem("Item 1",1)
    testmenu.addItem("Item 2",2)
    #testmenu.run()
    testmenu.addItem("Item 3",3)
    testmenu.addItem("Item 4",4)
    testmenu.addItem("Item 5",5)
    selection = testmenu.run()
    testmenu.rmItem(3)
    #selection = testmenu.run()
    if selection is 1:
        stdscr.addstr(1,1,"result: 1")
    elif selection is 2:
        stdscr.addstr(1,1,"result: 2")
    elif selection is 3:
        stdscr.addstr(1,1,"result: 3")
    elif selection is 4:
        stdscr.addstr(1,1,"result: 4")
    elif selection is 5:
        stdscr.addstr(1,1,"result: 5")
    else:
        stdscr.addstr(1,1,"Exited")
    stdscr.getch()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
