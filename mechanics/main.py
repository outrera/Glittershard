#!/usr/bin/python

""" mainmenu.py
    sets up screens to be used 
"""
import curses
#import entity

#init
stdscr = curses.initscr()
curses.curs_set(0)
curses.cbreak()
curses.noecho()
stdscr.keypad(1)

#colors
#xterm = 256 colors, 256 color pairs
if curses.has_colors():
    curses.start_color()
    #initial color pairs
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    #If more colors are allowed
    #if curses.can_change_color():

#draw
stdscr.attron(curses.color_pair(1))
stdscr.border()
stdscr.addstr(2,3, "Welcome to Glittershard's End!", curses.A_UNDERLINE|curses.A_BOLD)
choices = {0:"Find a game",1:"Host a game",2:"Make a character",3:"Make a map",4:"Make an item",5:"Credits",6:"Quit"}
for i in range(len(choices)):
    stdscr.addstr((2*i)+4,5,choices[i])

#operate
exit = False
select = 0
stdscr.addstr((select*2)+4,2,"=>",curses.color_pair(2))
while exit == False:
    key = stdscr.getch()
    if key == 27: #escape key
        exit = True
    elif key == 259: #dp
        stdscr.addstr((select*2)+4,2,"  ")
        select = select - 1
        if select < 0:
            select = len(choices)-1
    elif key == 258: #down
        stdscr.addstr((select*2)+4,2,"  ")
        select = select + 1
        if select > len(choices)-1:
            select = 0
    elif key == 10: #enter
#Main program is in here
#============================================================
        if select == 0: #Server lookup/connect
        elif select == 1: #Create server
        elif select == 2: #Make new character
        elif select == 3: #Make new map file
        elif select == 4: #Make new item file
        elif select == 5: #Display credits
        elif select == 6:
            exit = True
#============================================================
    stdscr.addstr((select*2)+4,2,"=>",curses.color_pair(2))

#Destroy window
curses.nocbreak()
curses.echo()
stdscr.keypad(0)
curses.endwin()
