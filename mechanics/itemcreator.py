#!/usr/bin/env python

""" itemcreator.py
    This program automatically opens/creates an .ini file to write values.
    
    Author: Jeremy Stintzcum
    Date last Modified: 11/1/17
    python ver: 2.7
"""
import ConfigParser
import menu, textin

#TODO Add .ini files
#TODO add the defs to all items
#TODO move the parser defs to a new file, so they can be reused

c = ConfigParser.SafeConfigParser()
if c.read("settings.ini") and c.has_section("itemcreator"):
    WIDTH = c.getint("itemcreator","width")
    HEIGHT = c.getint("itemcreator","height")
    STARTX = c.getint("itemcreator","startx")
    STARTY = c.getint("itemcreator","starty")
    TEXTBOXH = c.getint("itemcreator","textboxh")
    TEXTBOXW = c.getint("itemcreator","textboxw")
    DESCBOXH = c.getint("itemcreator","descboxh")
    DESCBOXW = c.getint("itemcreator","descboxw")
else:
    WIDTH = 80
    HEIGHT = 24
    STARTX = 0
    STARTY = 0
    TEXTBOXH = 4
    TEXTBOXW = 30
    DESCBOXH = 20
    DESCBOXW = 60

#Filenames
WFILE = "text.ini"
AFILE = "text.ini"
SFILE = "text.ini"
BFILE = "text.ini"
GFILE = "text.ini"
PFILE = "text.ini"

#Constants
TAB_KEY = ord("\t")
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

def createItem(self, itype, color = 0):
    """ createItem(itype, color)
    
        itype: The type of item
        color: Color of the textbox
    """
    #init
    c = ConfigParser.SafeConfigParser()
    nmenu = menu.Menu(STARTY,STARTX,HEIGHT,WIDTH,color,"Item Creator")
    
    def getFloat(c,name,tag,text):
        """Sets a float value"""
        temp = textin.TextIn(text,(HEIGHT/2)+STARTY,
        (WIDTH/2)+STARTX-(TEXTBOXW/2),TEXTBOXH,TEXTBOXW,color)
        try:
            temp = float(temp)
            "{0:.2g}".format(temp)
            temp = str(temp)
            c.set(name,tag,temp)
            nmenu.window.touchwin()
            nmenu.window.refresh()
        except:
            getFloat(c,name,tag,"Not a number:")
            
    def getInt(c,name,tag,text):
        """Sets an int value"""
        temp = textin.TextIn(text,(HEIGHT/2)+STARTY,
        (WIDTH/2)+STARTX-(TEXTBOXW/2),TEXTBOXH,TEXTBOXW,color)
        try:
            int(temp)
            temp = str(temp)
            c.set(name,tag,temp)
            nmenu.window.touchwin()
            nmenu.window.refresh()
        except:
            getInt(c,name,tag,"Not an Integer:")
    
    def getName(c):
        """Gets the section name"""
        name = textin.TextIn("Enter a name:",(HEIGHT/2)+STARTY,
        (WIDTH/2)+STARTX-(TEXTBOXW/2),TEXTBOXH,TEXTBOXW,color)
        while c.has_section(name):
            name = textin.TextIn("Item already exists.",(HEIGHT/2)+STARTY,
            (WIDTH/2)+STARTX-(TEXTBOXW/2),TEXTBOXH,TEXTBOXW,color)
        c.add_section(name)
        nmenu.window.touchwin()
        nmenu.window.refresh()
        return name
        
    def getDesc(c,name,tag):
        "Gets a description"
        temp = textin.TextIn("Description: (tab finishes)",
        (HEIGHT/2)+STARTY-(DESCBOXH/2),(WIDTH/2)+STARTX-(DESCBOXW/2),DESCBOXH,
        DESCBOXW,color,TAB_KEY)
        c.set(name,tag,temp)
        nmenu.window.touchwin()
        nmenu.window.refresh()
    
    def getBool(c,name,tag,text):
        curses.curs_set(0)
        boolmenu = menu.Menu((HEIGHT/2)+STARTY,
            (WIDTH/2)+STARTX-(TEXTBOXW/2),TEXTBOXH,TEXTBOXW,color,text)
        boolmenu.addItem("True",1)
        boolmenu.addItem("False",2)
        selection = boolmenu.run()
        if selection is 1:
            c.set(name,tag,"true")
        else:
            c.set(name,tag,"false")
        curses.curs_set(1)
        nmenu.window.touchwin()
        nmenu.window.refresh()
    
    #Choose an item type
    nmenu.addItem("Weapon",WEAPON)
    nmenu.addItem("Armor",ARMOR)
    nmenu.addItem("Shield",SHIELD)
    nmenu.addItem("Bag",BAG)
    nmenu.addItem("Gear",GEAR)
    nmenu.addItem("Potion",POTION)
    choice = nmenu.run()
    #Clear menu
    nmenu.clear()
    if choice is WEAPON:
        c.read(WFILE)
        name = getName(c)
        getFloat(c,name,"price","Set price:")
        getInt(c,name,"dietype","Type of Die:")
        getDesc(c,name,"desc")
        getFloat(c,name,"weight","Set weight:")
        getBool(c,name,"ap","Armor piercing?")
        #write to file
        f = open(WFILE,"wb")
        c.write(f)
        f.close()
    elif choise is ARMOR:
        c.read(AFILE)
        getName(c)
        getFloat(c,name,"price","Set price:")
        f = open(AFILE,"wb")
        c.write(f)
        f.close()
    elif choise is SHIELD:
        c.read(SFILE)
        getName(c)
        getFloat(c,name,"price","Set price:")
        f = open(SFILE,"wb")
        c.write(f)
        f.close()
    elif choise is BAG:
        c.read(BFILE)
        getName(c)
        getFloat(c,name,"price","Set price:")
        f = open(BFILE,"wb")
        c.write(f)
        f.close()
    elif choise is GEAR:
        c.read(GFILE)
        getName(c)
        getFloat(c,name,"price","Set price:")
        f = open(GFILE,"wb")
        c.write(f)
        f.close()
    elif choise is POTION:
        c.read(PFILE)
        getName(c)
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
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLUE)
    createItem(1,1)
    #reset
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(0)
    curses.endwin()
