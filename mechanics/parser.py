#!/usr/bin/python

""" parser.py
    Accepts a string and decides what to do with it. Also takes in the person 
    typing and a list of targets.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/20/17
    python ver: 2.7
"""
import re, curses, curses.panel
import ConfigParser
import textin, dice

#settings
c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("parser"):
    WIDTH = c.getint("parser","width")
    HEIGHT = c.getint("parser","height")
    DEFAULTCOLOR = c.getint("parser","defaultcolor")
else:
    WIDTH = 54
    HEIGHT = 4
    DEFAULTCOLOR = 1

#Constants
NOOFDICE = 0
DENOMINATION = 1
KEEPS = 2
KEEPHIGH = 3
ADD = 4
WHO = 5
ROLL = 0
ME = 1
WHISPER = 2
DM = 3
ITEMS = 4
TURN = 5
TYPE = 0
VALUE = 1

class Parser:
    def __init__(self, stdscr, roller, who):
        #init
        self.stdscr = stdscr
        self.Y, self.X = stdscr.getmaxyx()
        self.h = HEIGHT
        self.w = WIDTH
        self.x = 0
        self.y = self.Y-HEIGHT
        self.color = DEFAULTCOLOR
        self.keys = []
        self.roller = roller
        self.who = who
        self.out = {TYPE:-1, VALUE:None}
        #precompiled RegEx
        #sent strings
        self.roll = re.compile(r"/roll|!roll") #rolls dice
        self.me = re.compile(r"/me|!me") #Formats message to make it cinematic
        self.whisper = re.compile(r"/whisper|!whisper") #sends message to specifie player
        self.dm = re.compile(r"/dm|!dm") #sends message to DM
        self.items = re.compile(r"/items|!items") #open item menu
        self.turn = re.compile(r"/turn|!turn") #allows one to return to taking a turn 
        #dice
        self.num = re.compile(r"\d+")
        self.khigh = re.compile(r"high|High|h|HIGH")
        self.klow = re.compile(r"low|Low|LOW")
        self.add = re.compile(r"\+")
        self.sub = re.compile(r"-")
        self.dice = re.compile(r"\d+|\+|-|high|High|h|HIGH|low|Low|LOW")
        #draw
        curses.panel.update_panels()
        curses.doupdate() 
        
    def parse(self):
        string = textin.TextIn("Chat:",self.y,self.x,self.h,self.w,self.color)
        self.stdscr.refresh()
        self.out[TYPE] = ROLL
        if self.roll.match(string):
            self.keys = self.dice.findall(string)
            if not self.keys:
                return self.out
            out = {NOOFDICE:0, DENOMINATION:0, KEEPS:0, KEEPHIGH:True, 
            ADD:True,
            WHO:self.who}
            outlist = []
            while self.keys:
                if self.add.match(self.keys[0]):
                    out[ADD] = True
                    del self.keys[0]
                elif self.sub.match(self.keys[0]):
                    out[ADD] = False
                    del self.keys[0]
                elif self.num.match(self.keys[0]):
                    out[NOOFDICE] = int(self.keys[0])
                    out[KEEPS] = int(self.keys[0])
                    del self.keys[0]
                    if self.keys and self.num.match(self.keys[0]):
                        out[DENOMINATION] = int(self.keys[0])
                        del self.keys[0]
                        if self.keys and self.num.match(self.keys[0]):
                            out[KEEPS] = int(self.keys[0])
                            del self.keys[0]
                            if self.keys and self.khigh.match(self.keys[0]):
                                out[KEEPHIGH] = True
                                del self.keys[0]
                            elif self.keys and self.klow.match(self.keys[0]):
                                out[KEEPHIGH] = False
                                del self.keys[0]
                    outlist.append(out)
                    out = {NOOFDICE:0, DENOMINATION:0, KEEPS:0, KEEPHIGH:True, 
                    ADD:True, WHO:self.who}
                else:
                    del self.keys[0]
            if outlist:
                self.out[VALUE] = self.roller.Roll(outlist)
            return self.out
        elif self.me.match(string):
            pass
        elif self.whisper.match(string):
            pass
        elif self.dm.match(string):
            pass
        elif self.items.match(string):
            pass
        elif self.turn.match(string):
            pass
        else:
            self.out[VALUE] = string
            return self.out

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
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_RED)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_BLUE)
    roller = dice.Roller(stdscr,True)
    parser = Parser(stdscr, roller, 1)
    result = {VALUE:None}
    while result[VALUE] is not "":
        result = parser.parse()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
