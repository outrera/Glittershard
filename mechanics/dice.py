#!/usr/bin/env python

""" Dice.py
    This program rolls dice and returns a value
    
    Author: Jeremy Stintzcum
    Date last Modified: 10/15/17
    python ver: 2.7
"""
import random, curses, curses.panel

#TODO Move settings to file
#settings
BORDER = 0
DBORDER = 2 * BORDER
OFFSET = 1 + BORDER
DOFFSET = 2 * OFFSET
DIE_ROLLER_WIDTH = 24 + DOFFSET

class Roller:
    """ class Roller(stdscr, colorList, loud)
        The class that handles all window interactions
        
        stdscr: ncurses window with the terminal's y and x coordinates
        color: default color for the window
            0 is background
            1 is the DM
            2-256 are for players
        loud: determines how verbose the output is 
    """
    def __init__(self, stdscr, color=0, loud=False):
        self.Y, self.X = stdscr.getmaxyx()
        #init vars
        self.h = self.Y - DBORDER
        self.w = DIE_ROLLER_WIDTH
        self.y = BORDER
        self.x = self.X - (DIE_ROLLER_WIDTH + DBORDER)
        self.display = []
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

    def updateList(self, newlist, color = 0):
        """ updateList(string)
            Draws the output of the die roll and refreshes the panel
            
            newlist: List of strings to be drawn on screen
        """
        #add new entries to display list
        self.display.reverse()
        for i in range(len(newlist)):
            newlist[i] = "{message: <{width}}".format(message=newlist[i], 
            width=self.w-DOFFSET)
            #TODO make the strings auto-wrap when exceeding width of dice bar
            self.display.append((newlist[i],color))
        self.display.reverse()
        #remove older entries
        while len(self.display) >= (self.h-DOFFSET):
            self.display.pop()
        #draw the lines in the proper order
        for j in range(len(self.display)):
            self.window.addstr((self.h-OFFSET-1)-j,OFFSET, self.display[j][0], 
            curses.color_pair(self.display[j][1]))
        #update screen
        curses.panel.update_panels()
        curses.doupdate()

    def Roll(self, roll = []):
        """ roll(listofrolls)
            Parses a list of dictionaries of rolls, to roll several types of 
            dice at once. Returns integer value corresponding to the total of 
            dice rolled.
            
            roll: A list of dictionaries as so:
                dict = {#dice, denom, #keep, keeph, add, who}
        """
        #init
        lstring = [] #loud. Always sent to the server
        qstring = [] #quiet
        val = 0
        for i in range(len(roll)):
            #no dice, just a value
            if roll[i]["denom"] is 0:
                if roll[i]["add"] == False:
                    val = val - roll[i]["#dice"]
                    lstring.append("Subtracting "+str(roll[i]["#dice"]))
                    qstring.append("Subtracting "+str(roll[i]["#dice"]))
                else:
                    val += roll[i]["#dice"]
                    lstring.append("Adding "+str(roll[i]["#dice"]))
                    qstring.append("Adding "+str(roll[i]["#dice"]))
            else: #rolling dice
                lstring.append("Rolling %sd%s" %(roll[i]["#dice"],
                    roll[i]["denom"]))
                numlist = []
                for j in range(roll[i]["#dice"]):
                    numlist.append(random.randint(1,roll[i]["denom"]))
                lstring.append("Results: " + str(numlist))
                numlist.sort() #Order the rolls from high to low
                if roll[i]["keeph"] == False:
                    numlist.reverse() #low to high, pop the correct die values
                    lstring.append("Keeping %s low dice" %(roll[i]["#keep"]))
                else:
                    lstring.append("Keeping %s high dice" %(roll[i]["#keep"]))
                #only keep the dice wanted
                for j in range(roll[i]["#keep"]):
                    if roll[i]["add"] == False:
                        val = val - numlist.pop()
                        lstring.append("subtracting")
                    else:
                        lstring.append("adding")
                        val += numlist.pop()
        #Write total
        lstring.append("Total: " + str(val))
        qstring.append("Total: " + str(val))
        #update list
        if self.loud:
            self.updateList(lstring, roll[i]["who"]+1) #+1 is because who starts
        else:                                          #at 0, and colors start 
            self.updateList(qstring, roll[i]["who"]+1) #at 1
        #TODO send data to logger/network
        #return number for use
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
    dict2 = {"#dice":2, "denom":4, "#keep":2, "keeph":False, "add":True, "who":0}
    dict3 = {"#dice":3, "denom":0, "#keep":2, "keeph":True, "add":False, "who":1}
    dict4 = {"#dice":5, "denom":0, "#keep":2, "keeph":True, "add":True, "who":1}
    dict5 = {"#dice":2, "denom":4, "#keep":1, "keeph":False, "add":False, "who":2}
    dict6 = {"#dice":3, "denom":6, "#keep":2, "keeph":True, "add":False, "who":2}
    list1 = [dict1,dict2]
    list2 = [dict3,dict4]
    list3 = [dict4,dict5]
    val = roller.Roll(list1)
    stdscr.getch()
    val = roller.Roll(list2)
    stdscr.getch()
    val = roller.Roll(list3)
    stdscr.getch()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
