#!/usr/bin/python

""" classList.py
    Contains all class attributes
    Arg1: class to get attributes for
    Arg2: level of created class. used for perks
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
