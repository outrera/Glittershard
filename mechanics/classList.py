#!/usr/bin/python

""" classList.py
    
    !!!NOT A VALID FILE!!!
    
    This file remains until data can be stripped from it.
"""
#TODO: Add item and perk choice system
#TODO: Items and perks should be functional, not strings

import itemList, perkList, trainingList

#returns dictionary of attributes for string provided
def get(className):
    items = []
    training = []
    perks = []
    gold = 0
    if className is "assassin":
        items.extend("leather armor", "small bow", "quiver", "20 arrows", "standard kit")
        gold = 150
        training.extend("smallMelee", "bows", "lightArmor", "freerunning", "streetsmarts")
        perks.extend("balancedFighter", "goodPerch", "Shadowed")
        
    else:
        #Invalid class
        print className + " is not a valid class."
    #pack into tuple and return
    attri = items, gold, training, perks
    return arrti
