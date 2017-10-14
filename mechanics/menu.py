""" menu.py
    menu class for creating menus
    Supports creation of menu and menu items before the menu is called, and can 
    be modified at any time
"""
import curses, curses.panel
RUNNING = -2 #While loop condition
EXIT = -1 #exit condition
KEY_ESC = 27
KEY_ENTER = 10

#TODO Move settings to file

#settings
LINE_OFF = 2 #standard offset
BORDER = 1 #size of border
CURSOR = "=>" #cursor
CURSOR_CLR = "  " #same length as cursor
CURSOR_STARTPOS = 2 #starting x position of cursor
ITEM_OFF = len(CURSOR) + CURSOR_STARTPOS + BORDER #listed item offset

class Menu:
    def __init__(self,y,x,h,w,color=0,title=""):
        #init vars
        self.select = 0
        self.y = y
        self.x = x
        self.h = h
        self.w = w
        self.items = []
        self.color = color
        self.title = title
        #create window and set attributes
        self.window = curses.newwin(self.h,self.w,self.y,self.x)
        self.window.keypad(1)
        self.window.attrset(curses.color_pair(self.color))
        self.window.bkgd(" ",curses.color_pair(self.color))
        self.window.border()
        self.window.addstr((self.select*LINE_OFF)+LINE_OFF,CURSOR_STARTPOS,
        CURSOR)
        self.window.addstr(BORDER,BORDER,self.title,curses.A_BOLD|
        curses.A_UNDERLINE|curses.color_pair(self.color))
        for i in range(len(self.items)):
            self.window.addstr((LINE_OFF*i)+LINE_OFF,ITEM_OFF,
            self.items[i]["name"])
        #set panel
        self.panel = curses.panel.new_panel(self.window)

    """ run()
        Executes the menu, getting input and returning a    
        integer to select a function
    """
    def run(self):
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
                    self.select = len(self.items)-1
                self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
                CURSOR_STARTPOS,CURSOR)
            elif key == curses.KEY_DOWN: #down
                self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
                CURSOR_STARTPOS,CURSOR_CLR)
                self.select = self.select + 1
                if self.select > len(self.items)-1:
                    self.select = 0
                self.window.addstr((self.select*LINE_OFF)+LINE_OFF,
                CURSOR_STARTPOS,CURSOR)
            elif key == KEY_ENTER:
                state = self.select
            curses.panel.update_panels()
            curses.doupdate()
        testmenu.panel.hide()
        return self.items[state]["command"]
            
    """ newItem(name,command)
        create a new entry in the menu with name "name" and 
        an int for command. This int will be be returned 
        when the menu is run, selecting an action
    """
    def newItem(self,name,com=0):
        dict1 = {"name":name,"command":com}
        self.items.append(dict1)
        #update list
        for i in range(len(self.items)):
            self.window.addstr((LINE_OFF*i)+LINE_OFF,ITEM_OFF,
            self.items[i]["name"])
            
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
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLUE)
    testmenu = Menu(1,1,12,20,1,"Test")
    testmenu.newItem("foo",1)
    testmenu.newItem("bar",2)
    testmenu.newItem("nuke",3)
    testmenu.newItem("I like turtles",4)
    testmenu.newItem("oh god why",5)
    selection = testmenu.run()
    if selection is 1:
        stdscr.addstr(1,1,"Hello")
    elif selection is 2:
        stdscr.addstr(1,1,"Goodbye")
    elif selection is 3:
        stdscr.addstr(1,1,"From Russia with Love")
    elif selection is 4:
        stdscr.addstr(1,1,"MUDKIPZ")
    elif selection is 5:
        stdscr.addstr(1,1,"what is this i cant even")
    else:
        stdscr.addstr(1,1,"why")
    stdscr.getch()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
