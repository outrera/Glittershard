#!/usr/bin/python

""" itemlist.py

    !!!NOT A VALID FILE!!!
    
    This file remains until all valuable data is removed from it
"""

#TODO Add room keys for inns
#TODO Fix potions

#weapon class
class weapon:
    def __init__(self):
        self.attr = {"name":"Dagger", "price":1, "weight":0.5, "acc":1, "die":4,
        "#ofdie":1, "hand":1, "dtype":"blade", "ratt":True, "matt":True, 
        "size":"small","ap":False, "rnge":1, "slow":False, "brace":False, 
        "binds":False}
#armor class
class armor:
    def __init__(self):
        self.attr = {"name":"Cloth", "price":0, "ar":0, "weight":"none", "dexp":0}
#shields class
class shields:
    def __init__(self):
        self.attr = {"name":"Buckler", "price":5, "weight":5, "hand":0, "ar":1}
#bag class
class bag:
    def __init__(self):
        self.attr = {"name":"Backpack", "price":5, "cap":50, "wings":False, "shapeshift":False, "ammo":False}
#gear/ammo/medical/mfocus class
class gear:
    def __init__(self):
        self.attr = {"name":"Awl", "price":2, "weight":0.5}
#potions class
class potions:
    def __init__(self):
        self.attr = {}

def search(itemname = None):
    """A list of all items. If None is set, returns full list."""
    if itemname = None:
        return items
    elif itemname in items:
        return self.get(itemname)
    else:
        return None


#TODO move to INI
def get(itemName):
    if itemName is "dagger":
        return weapon()
    elif itemName is "axe":
        axe = weapon()
        axe.attr["name"] = "Axe"
        axe.attr["price"] = 2
        axe.attr["weight"] = 3
        axe.attr["die"] = 6
        axe.attr["ratt"] = False
        axe.attr["size"] = "medium"
        axe.attr["brace"] = True
        return axe
    elif itemName is "broadsword":
        broadsword = weapon()
        broadsword.attr["name"] = "Broadsword"
        broadsword.attr["price"] = 4
        broadsword.attr["weight"] = 5
        broadsword.attr["acc"] = 2
        broadsword.attr["die"] = 8
        broadsword.attr["hand"] = 2
        broadsword.attr["ratt"] = False
        broadsword.attr["size"] = "large"
        return broadsword
    elif itemName is "club":
        club = weapon()
        club.attr["name"] = "club"
        club.attr["weight"] = 4
        club.attr["die"] = 6
        club.attr["ratt"] = False
        club.attr["size"] = "medium"
        club.attr["dtype"] = "blunt"
        return club
    elif itemName is "crowbar":
        crowbar = weapon()
        crowbar.attr["name"] = "Crowbar"
        crowbar.attr["weight"] = 3
        crowbar.attr["price"] = 4
        crowbar.attr["acc"] = 2
        crowbar.attr["die"] = 6
        crowbar.attr["dtype"] = "blunt"
        crowbar.attr["size"] = "medium"
        crowbar.attr["ratt"] = False
        return crowbar
    elif itemName is "flail":
        flail = weapon()
        flail.attr["name"] = "Flail"
        flail.attr["price"] = 10
        flail.attr["weight"] = 2.5
        flail.attr["#ofdie"] = 2
        flail.attr["dtype"] = "blunt"
        flail.attr["size"] = "medium"
        flail.attr["ratt"] = False
        return flail
    elif itemName is "greataxe":
        greataxe = weapon()
        greataxe.attr["name"] = "Greataxe"
        greataxe.attr["price"] = 12
        greataxe.attr["weight"] = 6
        greataxe.attr["die"] = 12
        greataxe.attr["hand"] = 2
        greataxe.attr["size"] = "large"
        greataxe.attr["ratt"] = False
        return greataxe
    elif itemname is "hammer":
        hammer = weapon()
        hammer.attr["name"] = "Hammer"
        hammer.attr["price"] = 1
        hammer.attr["weight"] = 1
        hammer.attr["dtype"] = "blunt"
        
