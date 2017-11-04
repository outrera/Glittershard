#!/usr/bin/env python

""" itemhandler.py
    This program automatically opens/creates an .ini file to write values.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/2/17
    python ver: 2.7
"""
import ConfigParser
import menu, textin, configset

#TODO Add .ini files
#TODO add the defs to all items
#TODO Viewer
#TODO Modifier
#TODO Make into a class.
#TODO Add magical effects

c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("itemcreator"):
    WIDTH = c.getint("itemcreator","width")
    HEIGHT = c.getint("itemcreator","height")
    STARTX = c.getint("itemcreator","startx")
    STARTY = c.getint("itemcreator","starty")
else:
    WIDTH = 80
    HEIGHT = 24
    STARTX = 0
    STARTY = 0

#Filenames
WFILE = "weapons.ini"
AFILE = "text.ini"
SFILE = "text.ini"
BFILE = "text.ini"
GFILE = "text.ini"
PFILE = "text.ini"

#Menu options
NEW = 0
MODIFY = 1
VIEW = 2
#Itemtypes
WEAPON = 0
ARMOR = 1
SHIELD = 2
BAG = 3
GEAR = 4
POTION = 5
#Weapon attributes
BLUNT = 0
BLADE = 1
SMALL = 0
MEDIUM = 1
LARGE = 2
BOLT = 0
ARROW = 1
THROWN = 2

def itemHandler(color=0):
    """ createItem(itype, color)
    
        itype: The type of item
        color: Color of the textbox
    """
    #init
    c = ConfigParser.SafeConfigParser()
    nmenu = menu.Menu(STARTY,STARTX,HEIGHT,WIDTH,color,"Item Creator")
    #Choose 
    nmenu.addItem("New item",NEW)
    nmenu.addItem("Modify an item",MODIFY)
    nmenu.addItem("View an item",VIEW)
    choice1 = nmenu.run()
    nmenu.clear()
    #Choose an item type
    nmenu.addItem("Weapon",WEAPON)
    nmenu.addItem("Armor",ARMOR)
    nmenu.addItem("Shield",SHIELD)
    nmenu.addItem("Bag",BAG)
    nmenu.addItem("Gear",GEAR)
    nmenu.addItem("Potion",POTION)
    choice = nmenu.run()
    if choice is WEAPON:
        c.read(WFILE)
        name = configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,color,name,"price","Set price:")
        configset.getFloat(nmenu,c,color,name,"weight","Set weight:")
        configset.getBool(nmenu,c,color,name,"matt","Melee:")
        configset.getBool(nmenu,c,color,name,"ratt","Ranged:")
        configset.getInt(nmenu,c,color,name,"accuracy","Accuracy:")
        configset.getInt(nmenu,c,color,name,"dietype","Type of Die:")
        configset.getInt(nmenu,c,color,name,"noofdice","Number of Dice:")
        configset.getInt(nmenu,c,color,name,"hands","Min num of hands:")
        configset.getBool(nmenu,c,color,name,"slow","Slow action:")
        configset.getBool(nmenu,c,color,name,"binds","Binding:")
        configset.getBool(nmenu,c,color,name,"ap","Armor piercing?")
        if c.getboolean(name,"matt"):
            wm = menu.Menu(STARTY/4,STARTX/4,HEIGHT/2,WIDTH/2,color,"Damage type:")
            wm.addItem("Bladed",BLADE)
            wm.addItem("Blunt",BLUNT)
            choice = wm.run()
            if choice is BLADE:
                c.set(name,"dtype",str(BLADE))
            elif choice is BLUNT:
                c.set(name,"dtype",str(BLUNT))
            nmenu.window.touchwin()
            nmenu.winodw.clear()
            configset.getInt(nmenu,c,color,name,"mrange","Melee range in units:")
            configset.getBool(nmenu,c,color,name,"brace","Weapon cam be braced:")
        if c.getboolean(name,"ratt"):
            configset.getInt(nmenu,c,color,name,"rrange","Max range:")
            rm = menu.Menu(STARTY/4,STARTX/4,HEIGHT/2,WIDTH/2,color,"Damage type:")
            rm.addItem("Thrown",THROWN)
            rm.addItem("Arrow",ARROW)
            rm.addItem("Bolt",BOLT)
            choice = rm.run()
            if choice is THROWN:
                c.set(name,"dtype",str(THROWN))
            elif choice is ARROW:
                c.set(name,"dtype",str(ARROW))
            elif choice is BOLT:
                c.set(name,"dtype",str(BOLT))
            nmenu.window.touchwin()
            nmenu.winodw.clear()
            configset.getBool(nmenu,c,color,name,"loadisaction","Load is an action")
            configset.getBool(nmenu,c,color,name,"windisaction","Winds up")
            c.set(name,"wound","false")
        configset.getDesc(nmenu,c,color,name,"desc")
        #write to file
        f = open(WFILE,"wb")
        c.write(f)
        f.close()
    elif choise is ARMOR:
        c.read(AFILE)
        configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,color,name,"price","Set price:")
        f = open(AFILE,"wb")
        c.write(f)
        f.close()
    elif choise is SHIELD:
        c.read(SFILE)
        configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,color,name,"price","Set price:")
        f = open(SFILE,"wb")
        c.write(f)
        f.close()
    elif choise is BAG:
        c.read(BFILE)
        configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,color,name,"price","Set price:")
        f = open(BFILE,"wb")
        c.write(f)
        f.close()
    elif choise is GEAR:
        c.read(GFILE)
        configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,color,name,"price","Set price:")
        f = open(GFILE,"wb")
        c.write(f)
        f.close()
    elif choise is POTION:
        c.read(PFILE)
        configset.getName(nmenu,c,color)
        f = open(PFILE,"wb")
        c.write(f)
        f.close()
    else:
        pass
#Test code
if __name__ == "__main__":
    import curses
    #init
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    curses.start_color()
    #test
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    createItem(1)
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
