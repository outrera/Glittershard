#!/usr/bin/env python

""" itemhandler.py
    This program automatically opens/creates an .ini file to write values.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/20/17
    python ver: 2.7
"""
import ConfigParser
import menu, textin, configset

#TODO Add .ini files
#TODO add the defs to all items
#TODO Viewer
#TODO Modifier
#TODO Make item into class
#TODO Add magical effects

c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("itemcreator"):
    WIDTH = c.getint("itemcreator","width")
    HEIGHT = c.getint("itemcreator","height")
    STARTX = c.getint("itemcreator","startx")
    STARTY = c.getint("itemcreator","starty")
    DEFAULTCOLOR = c.getint("itemcreator","defaultcolor")
else:
    WIDTH = 80
    HEIGHT = 24
    STARTX = 0
    STARTY = 0
    DEFAULTCOLOR = 0

#Filenames
WFILE = "weapons.ini"
AFILE = "armor.ini"
SFILE = "shields.ini"
BFILE = "bags.ini"
GFILE = "gear.ini"
PFILE = "potions.ini"

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

def itemHandler(color=-1):
    """ createItem(itype, color)
    
        itype: The type of item
        color: Color of the textbox
    """
    #init
    if color is -1:
        color = DEFAULTCOLOR
    c = ConfigParser.SafeConfigParser()
    nmenu = menu.Menu(STARTY,STARTX,HEIGHT,WIDTH,"Item Creator",color)
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
        configset.getFloat(nmenu,c,name,"price","Set price:")
        configset.getFloat(nmenu,c,name,"weight","Set weight:")
        configset.getBool(nmenu,c,name,"matt","Melee:")
        configset.getBool(nmenu,c,name,"ratt","Ranged:")
        configset.getInt(nmenu,c,name,"accuracy","Accuracy:")
        configset.getInt(nmenu,c,name,"dietype","Type of Die:")
        configset.getInt(nmenu,c,name,"noofdice","Number of Dice:")
        configset.getInt(nmenu,c,name,"hands","Min num of hands:")
        configset.getBool(nmenu,c,name,"slow","Slow action:")
        configset.getBool(nmenu,c,name,"binds","Binding:")
        configset.getBool(nmenu,c,name,"ap","Armor piercing?")
        if c.getboolean(name,"matt"):
            wm = menu.Menu(HEIGHT/4,WIDTH/4,HEIGHT/2,WIDTH/2,"Damage type:",
            DEFAULTCOLOR)
            wm.addItem("Bladed",BLADE)
            wm.addItem("Blunt",BLUNT)
            choice = wm.run()
            if choice is BLADE:
                c.set(name,"dtype",str(BLADE))
            elif choice is BLUNT:
                c.set(name,"dtype",str(BLUNT))
            nmenu.refresh()
            configset.getInt(nmenu,c,name,"mrange",
            "Melee range in units:")
            configset.getBool(nmenu,c,name,"brace",
            "Weapon cam be braced:")
        if c.getboolean(name,"ratt"):
            configset.getInt(nmenu,c,name,"rrange","Max range:")
            rm = menu.Menu(HEIGHT/4,WIDTH/4,HEIGHT/2,WIDTH/2,
            "Damage type:",DEFAULTCOLOR)
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
            nmenu.refresh()
            configset.getBool(nmenu,c,name,"loadisaction",
            "Load is an action")
            configset.getBool(nmenu,c,name,"windisaction","Winds up")
            c.set(name,"wound","false")
        configset.getDesc(nmenu,c,name,"desc")
        #write to file
        f = open(WFILE,"wb")
        c.write(f)
        f.close()
        c.read(AFILE)
    elif choice is ARMOR:
        name = configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,name,"price","Set price:")
        configset.getFloat(nmenu,c,name,"weight","Set weight:")
        configset.getDesc(nmenu,c,name,"desc")
        f = open(AFILE,"wb")
        c.write(f)
        f.close()
    elif choice is SHIELD:
        c.read(SFILE)
        name = configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,name,"price","Set price:")
        configset.getFloat(nmenu,c,name,"weight","Set weight:")
        configset.getDesc(nmenu,c,name,"desc")
        f = open(SFILE,"wb")
        c.write(f)
        f.close()
    elif choice is BAG:
        c.read(BFILE)
        name = configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,name,"price","Set price:")
        configset.getDesc(nmenu,c,name,"desc")
        f = open(BFILE,"wb")
        c.write(f)
        f.close()
    elif choice is GEAR:
        c.read(GFILE)
        name = configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,name,"price","Set price:")
        configset.getFloat(nmenu,c,name,"weight","Set weight:")
        configset.getDesc(nmenu,c,name,"desc")
        f = open(GFILE,"wb")
        c.write(f)
        f.close()
    elif choice is POTION:
        c.read(PFILE)
        name = configset.getName(nmenu,c,color)
        configset.getFloat(nmenu,c,name,"price","Set price:")
        configset.getFloat(nmenu,c,name,"weight","Set weight:")
        configset.getDesc(nmenu,c,name,"desc")
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
    itemHandler(1)
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
