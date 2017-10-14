""" Dice.py
    This program rolls dice
    It includes a display module and a string parser
"""
import random, curses, curses.panel

#TODO log all die events
#TODO send ncurses over network
#TODO Move settings to file

#settings
BORDER = 0
BKGD_COLOR = 0
OFFSET = 1 + BORDER
DIE_ROLLER_WIDTH = 24 + (OFFSET*2)

""" class Roller(stdscr,colorList)
    The class that handles all window interactions
    it uses the stdscr to get window size, and takes in three colors:
    0 is background
    1 is other players and self
    2 is DM
    loud determines how verbose the output is 
"""
class Roller:
    def __init__(self, stdscr, color=0, loud=False):
        self.Y, self.X = stdscr.getmaxyx()
        #init vars
        self.h = self.Y - (2*BORDER)
        self.w = DIE_ROLLER_WIDTH
        self.y = BORDER
        self.x = self.X - (DIE_ROLLER_WIDTH + (BORDER*2))
        self.li = []
        self.loud = loud
        self.color = color
        #set window
        self.window = curses.newwin(self.h,self.w,self.y,self.x)
        self.window.attrset(curses.color_pair(self.color))
        self.window.bkgd(" ",curses.color_pair(self.color))
        self.window.border()
        #set panel
        self.panel = curses.panel.new_panel(self.window)
        #draw
        curses.panel.update_panels()
        curses.doupdate()

    """ updateList(string)
        The most recent roll of the die is displayed at the bottom of the queue.
        Colors are maintained
    """
    def updateList(self, string, color = BKGD_COLOR):
        self.li.reverse()
        for i in range(len(string)):
            string[i] = "{message: <{width}}".format(message=string[i], 
            width=self.w-2)
            self.li.append((string[i],color))
        self.li.reverse()
        while len(self.li) >= (self.h-(OFFSET*2)):
            self.li.pop()
        for j in range(len(self.li)):
            self.window.addstr((self.h-OFFSET-1)-j,1,self.li[j][0],
            curses.color_pair(self.li[j][1]))
        curses.panel.update_panels()
        curses.doupdate()

    """ roll(listofrolls)
        parses a list of dictionaries of rolls, to roll several types of dice at
        once. Returns integer value
        dict = {#dice, denom, #keep, keeph, add}
    """
    def Roll(self, roll = []):
        outstring = []
        val = 0
        for i in range(len(roll)):
            #no dice, just a value
            if roll[i]["denom"] is 0:
                if roll[i]["add"] == False:
                    val = val - roll[i]["#dice"]
                    if self.loud:
                        outstring.append("Subtracting "+str(roll[i]["#dice"]))
                else:
                    val += roll[i]["#dice"]
                    if self.loud:
                        outstring.append("Adding "+str(roll[i]["#dice"]))
            else: #rolling dice
                outstring.append("Rolling %sd%s" %(roll[i]["#dice"],
                    roll[i]["denom"]))
                numlist = []
                for j in range(roll[i]["#dice"]):
                    numlist.append(random.randint(1,roll[i]["denom"]))
                if self.loud:
                    outstring.append("Results: " + str(numlist))
                numlist.sort()
                if roll[i]["keeph"] == False:
                    numlist.reverse()
                    if self.loud:
                        outstring.append("Keeping %s low dice" 
                        %(roll[i]["#keep"]))
                else:
                    if self.loud:
                        outstring.append("Keeping %s high dice" 
                        %(roll[i]["#keep"]))
                for j in range(roll[i]["#keep"]):
                    if roll[i]["add"] == False:
                        val = val - numlist.pop()
                        outstring.append("subtracting")
                    else:
                        outstring.append("adding")
                        val += numlist.pop()
        outstring.append("Total: " + str(val))
        #update list
        self.updateList(outstring, roll[i]["who"]+1)
        #return number for use
        outstring = []
        return val
        
#Test code
if __name__ == "__main__":
    #init
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    curses.start_color()
    #test
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_MAGENTA,curses.COLOR_GREEN)
    roller = Roller(stdscr, 1, True)
    dict1 = {"#dice":2, "denom":6, "#keep":1, "keeph":True, "add":True, "who":0}
    dict2 = {"#dice":6, "denom":10, "#keep":1, "keeph":True, "add":True, "who":0}
    dict3 = {"#dice":3, "denom":0, "#keep":2, "keeph":True, "add":False, "who":1}
    dict4 = {"#dice":5, "denom":0, "#keep":2, "keeph":True, "add":True, "who":1}
    dict5 = {"#dice":2, "denom":4, "#keep":1, "keeph":False, "add":False, "who":2}
    dict6 = {"#dice":3, "denom":5, "#keep":2, "keeph":True, "add":True, "who":2}
    dict7 = {"#dice":3, "denom":5, "#keep":2, "keeph":True, "add":True, "who":2}
    dict8 = {"#dice":3, "denom":0, "#keep":2, "keeph":True, "add":True, "who":2}
    list1 = [dict1,dict2,dict3,dict4,dict5,dict6,dict7]
    list2 = [dict3,dict4]
    list3 = [dict4,dict5]
    val = roller.Roll(list1)
    stdscr.addstr(1,1,str(val))
    stdscr.getch()
    val = roller.Roll(list2)
    stdscr.addstr(2,1,str(val))
    stdscr.getch()
    val = roller.Roll(list3)
    stdscr.addstr(3,1,str(val))
    stdscr.getch()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
