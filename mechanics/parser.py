#!/usr/bin/python

""" parser.py
    Accepts a string and decides what to do with it. Also takes in the person 
    typing and a list of targets.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/4/17
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
else:
    WIDTH = 56
    HEIGHT = 4

#Constants
NOOFDICE = 0
DENOMINATION = 1
KEEPS = 2
KEEPHIGH = 3
ADD = 4
WHO = 5

class Parser:
    def __init__(self, stdscr, color):
        #init
        self.Y, self.X = stdscr.getmaxyx()
        self.h = HEIGHT
        self.w = WIDTH
        self.x = 0
        self.y = self.Y-HEIGHT
        self.color = color
        self.keys = []
        #precompiled RegEx
        #sent strings
        roll = re.compile(r"/roll|!roll")
        #dice
        num = re.compile(r"\d+")
        khigh = re.compile(r"high|High|h|HIGH")
        klow = re.compile(r"low|Low|l|LOW")
        add = re.compile(r"\+")
        sub = re.compile(r"-")
        dice = re.compile(r"\d+|\+|-|high|High|h|HIGH|low|Low|l|LOW")
        #draw
        curses.panel.update_panels()
        curses.doupdate() 
        
    def parse(self):
        string = textin.TextIn("Chat:",self.y,self.x,self.h,self.w,self.color)
        if roll.match(string):
            self.keys = dice.findall()
            out = {NOOFDICE:0, DENOMINATION:0, KEEPS:0, KEEPHIGH:True, ADD:True,
            WHO:0}
            print self.keys
            #while self.keys:
             #   if self.keys[0] is num.match()

#test code
if __name__ == "__main__":
    #init
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.cbreak()
    curses.echo()
    stdscr.keypad(1)
    curses.start_color()
    #test code
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_RED)
    parser = Parser(stdscr,1)
    parser.parse()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
"""
#Processes
say = 0
die = 1
me = 2
error = -1

#Parser func
def parser(string, user = "default", playerlist = ["John"]):
    output = {"from":user,"to":"all","type":say,"result":"none"}
    # !roll 2d6k1 low
    if re.match(r"/roll \d+d\d|!roll \d+d\d", string):
        temp = re.findall(r"\d+|\+|low|high", string)
        total = 0
        arr = []
        while temp:
            if temp[0] == "low":
                arr.append(0)
            elif temp[0] == "high":
                arr.append(1)
            elif temp[0] == "+":
                total += dice.roll(*arr)
                arr = []
            else:
                arr.append(int(temp[0]))
            del temp[0]
        total += dice.roll(*arr)
        output["type"] = die
        output["result"] = total
    #me
    elif re.match(r"/me |!me ", string):
        temp = re.sub(r"/me |!me ","", string)
        output["type"] = me
        output["result"] = temp
    #whisper
    elif re.match(r"/whisper |!whisper ", string):
        temp = re.sub(r"/whisper |!whisper ","",string)
        name = re.split(r"[^\w]+",temp)
        if name[0] not in playerlist:
            temp = "No player by name " + str(name[0])
            output["type"] = error
        else:
            temp = re.sub(r"[\w]+\s","",temp, 1)
            output["to"] = name[0]
#{"type":message,"result":temp,"from":user,"to":str(name[0])}
        output["result"] = temp
    #Send message to DM
    elif re.match(r"/dm |!dm ", string):
        temp = re.sub(r"/dm |!dm ","", string)
        output["to"] = "dm"
        output["result"] = temp
"""
