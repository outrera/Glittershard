#!/usr/bin/env python

""" Dice.py
    This program rolls dice and returns a value
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/20/17
    python ver: 2.7
"""
import random, curses, curses.panel
import ConfigParser

#settings
c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("dice"):
    BORDER = c.getint("dice","border")
    WIDTH = c.getint("dice","width")
    START_Y = c.getint("dice","starty")
    DEFAULTCOLOR = c.getint("dice","defaultcolor")
else:
    BORDER = 1
    WIDTH = 24
    START_Y = 0
    DEFAULTCOLOR = 1

#Constants
DBORDER = 2 * BORDER
DIE_ROLLER_WIDTH = WIDTH + DBORDER
NOOFDICE = 0
DENOMINATION = 1
KEEPS = 2
KEEPHIGH = 3
ADD = 4
WHO = 5

class Roller:
    """ class Roller(stdscr, loud)
        The class that handles all window interactions
        
        stdscr: ncurses window with the terminal's y and x coordinates
        color: default color for the window
            0 is background
            1 is the DM
            2-256 are for players
        loud: determines how verbose the output is 
    """
    def __init__(self, stdscr, loud=False):
        self.Y, self.X = stdscr.getmaxyx()
        #init vars
        self.h = self.Y
        self.w = DIE_ROLLER_WIDTH
        self.y = START_Y
        self.x = self.X - (DIE_ROLLER_WIDTH)
        self.display = []
        self.loud = loud
        self.color = DEFAULTCOLOR
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
            width=WIDTH)
            self.display.append((newlist[i],color))
        self.display.reverse()
        #remove older entries
        while len(self.display) >= (self.h-DBORDER):
            self.display.pop()
        #draw the lines in the proper order
        for j in range(len(self.display)):
            #TODO Truncate lines to fit display window if too large. 
            self.window.addstr((self.h-BORDER-1)-j,BORDER, self.display[j][0], 
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
        i = 0
        for i in range(len(roll)):
            #no dice, just a value
            if roll[i][DENOMINATION] is 0:
                if roll[i][ADD] == False:
                    val = val - roll[i][NOOFDICE]
                    lstring.append("Subtracting "+str(roll[i][NOOFDICE]))
                    qstring.append("Subtracting "+str(roll[i][NOOFDICE]))
                else:
                    val += roll[i][NOOFDICE]
                    lstring.append("Adding "+str(roll[i][NOOFDICE]))
                    qstring.append("Adding "+str(roll[i][NOOFDICE]))
            else: #rolling dice
                lstring.append("Rolling %sd%s" %(roll[i][NOOFDICE],
                    roll[i][DENOMINATION]))
                numlist = []
                for j in range(roll[i][NOOFDICE]):
                    numlist.append(random.randint(1,roll[i][DENOMINATION]))
                lstring.append("Results: " + str(numlist))
                numlist.sort() #Order the rolls from high to low
                if roll[i][KEEPHIGH] == False:
                    numlist.reverse() #low to high, pop the correct die values
                    lstring.append("Keeping %s low dice" %(roll[i][KEEPS]))
                else:
                    lstring.append("Keeping %s high dice" %(roll[i][KEEPS]))
                #only keep the dice wanted
                for j in range(roll[i][KEEPS]):
                    if roll[i][ADD] == False:
                        val = val - numlist.pop()
                    else:
                        val += numlist.pop()
        #Write total
        lstring.append("Total: " + str(val))
        qstring.append("Total: " + str(val))
        #update list
        if self.loud:
            self.updateList(lstring, roll[i][WHO]+1) #+1 is because who starts
        else:                                          #at 0, and colors start 
            self.updateList(qstring, roll[i][WHO]+1) #at 1
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
    roller = Roller(stdscr, True)
    dict1 = {NOOFDICE:2, DENOMINATION:6, KEEPS:1, KEEPHIGH:True, ADD:True, WHO:0}
    dict2 = {NOOFDICE:2, DENOMINATION:4, KEEPS:2, KEEPHIGH:False, ADD:True, WHO:0}
    dict3 = {NOOFDICE:3, DENOMINATION:0, KEEPS:2, KEEPHIGH:True, ADD:False, WHO:1}
    dict4 = {NOOFDICE:5, DENOMINATION:0, KEEPS:2, KEEPHIGH:True, ADD:True, WHO:1}
    dict5 = {NOOFDICE:2, DENOMINATION:4, KEEPS:1, KEEPHIGH:False, ADD:False, WHO:2}
    dict6 = {NOOFDICE:3, DENOMINATION:6, KEEPS:2, KEEPHIGH:True, ADD:False, WHO:2}
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
