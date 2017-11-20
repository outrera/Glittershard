#!/usr/bin/env python

""" menu.py
    Supports creation of menu and menu items before the menu is called, 
    and can be modified at any time
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/20/17
    python ver: 2.7
"""
import curses, curses.panel, ConfigParser

c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("menu"):
    BORDER = c.getint("menu","border")
    CURSOR = c.get("menu","cursor")
    CURSOR_STARTPOS = c.getint("menu","cursorstartpos")
    LINE_OFF = c.getint("menu","lineoff")
    TEXT_OFF = c.getint("menu","textoff")
    TITLE_OFF = c.getint("menu","titleoff")
    DEFAULTCOLOR = c.getint("menu","defaultcolor")
else:
    BORDER = 1 #size of border
    CURSOR = "=>" #cursor
    CURSOR_STARTPOS = 2 #starting x position of cursor
    LINE_OFF = 2 #standard offset
    TEXT_OFF = 0 #Space between title and first entry
    TITLE_OFF = 0 #Space between border and title
    DEFAULTCOLOR = 0

#Constants
EXIT = -1 #exit condition
ITEM_OFF = len(CURSOR) + CURSOR_STARTPOS + BORDER #listed item offset
temp = ""
for i in range(len(CURSOR)):
    temp = temp + " "
CURSOR_CLR = temp
KEY_ESC = 27
KEY_ENTER = ord("\n")
RUNNING = -2 #While loop condition

class Menu:
    """ Menu(y, x, h, w, title, color)
        Creates a menu with the given parameters
        
        y: y offset
        x: x offset
        h: horizontal height
        v: vertical width
        color: the color the menu will appear as
        title: Title text
    """
    def __init__(self,y,x,h,w,title="",color=-1):
        #init vars
        self.w = w
        #set minimum height
        if h < (2*BORDER+TEXT_OFF+TITLE_OFF+5):
            h = (2*BORDER+TEXT_OFF+TITLE_OFF+2*LINE_OFF+1)
        self.select = 0
        self.items = []
        self.page = 0
        if color >= 0:
            self.color = color
        else:
            self.color = DEFAULTCOLOR
        self.title = title
        self.maxlistsize = (h-(2*BORDER+TEXT_OFF+TITLE_OFF))/LINE_OFF
        self.maxpage = 0
        #create window and set attributes
        self.window = curses.newwin(h,w,y,x)
        self.window.keypad(1)
        self.window.attrset(curses.color_pair(color))
        self.window.bkgd(" ",curses.color_pair(color))
        self.window.border()
        self.window.addstr((self.select*LINE_OFF)+LINE_OFF,CURSOR_STARTPOS,
        CURSOR)
        self.window.addstr(BORDER+TITLE_OFF, BORDER, self.title, 
        curses.A_BOLD|curses.A_UNDERLINE|curses.color_pair(self.color))
        self.update()
        #set panel
        self.panel = curses.panel.new_panel(self.window)

    def refresh(self):
        """clears and refreshes the window"""
        self.update()
        self.window.refresh()

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
                len(self.items) > self.maxlistsize): #If next page
                    self.page = self.page + 1
                    if self.page > self.maxpage:
                        self.page = 0
                    state = RUNNING
                    self.update()
                #If an actual choice
                elif (state+self.page*(self.maxlistsize-1)) < len(self.items):
                    return self.items[state+(self.page*(self.maxlistsize-1))][1]
                else: #If blank
                    state = RUNNING
                    self.select = 0
                    self.update()
                    
    def update(self):
        """Updates window"""
        #Redraw
        self.window.clear()
        self.window.border()
        self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
        CURSOR_STARTPOS,CURSOR)
        self.window.addstr(BORDER,BORDER,self.title,curses.A_BOLD|
        curses.A_UNDERLINE|curses.color_pair(self.color))
        #Draw list
        if len(self.items) <= self.maxlistsize:#Entire list fits into one window
            for i in range(len(self.items)):
                self.window.addstr((LINE_OFF*i)+LINE_OFF,ITEM_OFF,
                self.items[i][0])
        else: #List must be broken up into pages
            for i in range(self.maxlistsize-1):
                if i+(self.maxlistsize-1)*self.page < len(self.items):
                    self.window.addstr((LINE_OFF*i)+LINE_OFF,ITEM_OFF,
                    self.items[i+(self.maxlistsize-1)*self.page][0])
            self.window.addstr((LINE_OFF*self.maxlistsize),ITEM_OFF,"Next Page")
            
    def addItem(self,name,com=0):
        """ addItem(name,command)
            Adds a new item to the menu and refreshes panels
            
            name: the displayed string
            command: int value to be returned on selection
        """
        name = "{message: <{width}}".format(message=name, 
        width=self.w-ITEM_OFF-2)
        tup = (name,com)
        self.items.append(tup) #Add new item
        self.maxpage = len(self.items)/(self.maxlistsize-1)
    
    def rmItem(self, command):
        """ rmItem(command)
            Removes an item from the menu and refreshes panels
            
            command: the int value of the "command" attribute of the dict
        """
        self.select = 0 #resets to avoid the selection of a null case
        for i in range(len(self.items)-1):
            if self.items[i][1] is command:
                self.items.pop(i) #Pop the unwanted item
        self.maxpage = len(self.items)/(self.maxlistsize-1) #Resize pages
        
    def clear(self):
        """ clear()
            Removes all items from menu
        """
        self.select = 0 #resets to avoid the selection of a null case
        while self.items:
            self.items.pop() #Pop everything
        self.maxpage = len(self.items)/(self.maxlistsize-1) #Resize pages
            
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
    curses.init_pair(1,curses.COLOR_MAGENTA,curses.COLOR_CYAN)
    testmenu = Menu(1,1,12,60,"Test")
    testmenu.addItem("Item 1",1)
    testmenu.addItem("Item 2",2)
    testmenu.run()
    testmenu.addItem("Item 3",3)
    testmenu.addItem("Item 4",4)
    testmenu.addItem("Item 5",5)
    testmenu.addItem("Item 6",6)
    testmenu.addItem("Item 7",7)
    testmenu.addItem("Item 8",8)
    testmenu.addItem("Item 9",9)
    selection = testmenu.run()
    testmenu.clear()
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
    elif selection is 6:
        stdscr.addstr(1,1,"result: 6")
    elif selection is 7:
        stdscr.addstr(1,1,"result: 7")
    elif selection is 8:
        stdscr.addstr(1,1,"result: 8")
    elif selection is 9:
        stdscr.addstr(1,1,"result: 9")
    else:
        stdscr.addstr(1,1,"Exited")
    stdscr.getch()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
