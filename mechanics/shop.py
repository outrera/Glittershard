#!/usr/bin/env python

""" shop.py
    shop class for handling gold transactions
    
    Desc: Contains the shop class, and all functions for buying and selling 
    items.
    Author: Jeremy Stintzcum
    Date last Modified: 10/31/17
    python ver: 2.7
"""

import menu, items
ALCHEMIST = 0
BLACKSMITH = 1
BOOKSTORE = 2
BOWER = 3
HUMANOIDMARKET = 4
INN = 5
JEWELERS = 6
MARKET = 7
PET = 8
SUPPLY = 9
TANNER = 10
WIZARD = 11

class Shop:
    """ Shop(x, y, w, h, name, typeofshop, player, color)
        Creates a shop
        
        name = The name of the shop
        shoptype = the type of shop (blacksmith, market, etc)
        player = player accessing the shop
        color = color of the shop window
        x, y, h, w = positional setup
    """
    def __init__(self, y, x, h, w, color, name, shoptype, player):
        """Defines shop and sets up items"""
        self.menu = Menu(y, x, h, w, color, name)
        self.shoptype = shoptype
        self.player = player
        self.items = []
        if shoptype is ALCHEMIST:
            #Get list of all items to be sold here, return name strings
            #Add all items than can be purchased at Alchemist to menu
            #Do this for all shops
        elif shoptype is BLACKSMITH:
        elif shoptype is BOOKSTORE:
        elif shoptype is BOWER:
        elif shoptype is HUMANIODMARKET:
        elif shoptype is INN:
        elif shoptype is JEWELERS:
        elif shoptype is MARKET:
        elif shoptype is PET:
        elif shoptype is SUPPLY:
        elif shoptype is TANNER:
        elif shoptype is WIZARD:
        else:
        
    def run(Self):
        """Runs the given shop."""
        item = itemList.get(self.items[self.menu.run()])
        if player.gold > item.attr["price"]:
            player.gold = player.gold - item.attr["price"]
            return item
        else:
            #TODO Tell player not enough money 
                
                
    def addItem(self, item):
        
    
    def rmItem(self, item):
    
#test code
if __name__ == "__main__":
    #init
    import curses, curses.panel
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    curses.start_color()
    #test code

    stdscr.getch()
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
