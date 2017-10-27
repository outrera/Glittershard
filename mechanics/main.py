#!/usr/bin/python

""" main.py
    Runs Glittershard 
    
    Author: Jeremy Stintzcum
    Date last Modified: 10/28/17
    python ver: 2.7
"""
import curses
import menu

#init
stdscr = curses.initscr()
curses.curs_set(0)
curses.cbreak()
curses.noecho()
stdscr.keypad(1)
Y, X = stdscr.getmaxyx()

#colors
#xterm = 256 colors, 256 color pairs
if curses.has_colors():
    curses.start_color()
    #initial color pairs
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    #TODO add more colors
    #If more colors are allowed
    #if curses.can_change_color():

#init menus
main = menu.Menu(5,1,Y-6,X-2,1,"Main Menu")
playermenu = menu.Menu(5,1,Y-6,X-2,2,"Player Options")
dmmenu = menu.Menu(5,1,Y-6,X-2,2,"DM Options")
#init items
main.addItem("Player", 0)
main.addItem("DM", 1)
main.addItem("Credits", 2)
main.addItem("Quit", -1)
playermenu.addItem("Find a game", 0)
playermenu.addItem("Make a character", 1)
playermenu.addItem("Load a character", 2)
dmmenu.addItem("Host a game", 0)
dmmenu.addItem("Make a map", 1)
dmmenu.addItem("Make an item", 2)
dmmenu.addItem("Make an NPC", 3)

#runtime
stdscr.attron(curses.color_pair(1))
stdscr.border()
stdscr.addstr(2,3, "Welcome to Glittershard's End!", 
curses.A_UNDERLINE|curses.A_BOLD)
stdscr.refresh()
selection = main.run()
if selection is 0: #Player
    selection = playermenu.run()
elif selection is 1: #DM
    selection = dmmenu.run()
elif selection is 2: #credits
    stdscr.addstr(3,3, "Jeremy Stintzcum made this pile of $#!7", 
curses.A_UNDERLINE|curses.A_BOLD)
    stdscr.getch()
elif selection is -1: #Quit
    pass
else:
    pass
    
#TODO Make menu functions work
#TODO catch exit conditions and have them restart the window above them
#TODO fix credits

#Destroy window
curses.nocbreak()
curses.echo()
stdscr.keypad(0)
curses.endwin()
