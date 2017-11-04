#!/usr/bin/python

""" entity.py
    Base Class of all moving creatures in Glittershard
    
    Author: Jeremy Stintzcum
    Date last Modified: 10/31/17
    python ver: 2.7
"""
import random

#TODO Change dict keys from strings to ints
#TODO Redesign system to accept .ini files
#TODO Right now this makes a player. Maybe make a lower lever entity that the player then fills?

class entity:
    #Initialization
    def __init__(self, owner):
        #main
        self.main = {"owner" : owner, "race" : "human", "clss" : None, 
        "level" : 1, "xp" : 0, "armor" : 0, "dodge" : 0, "speed" : 30, 
        "size" : "med"}
        #affiliations are used to determine enemies, friends, and neutrals in 
        #combat
        self.aff = []
        
        #stats
        self.stats = {"cha" : 0, "dm" : 0, "dex" : 0, "hea" : 0, "lm" : 0,  
        "str" : 0, "sur" : 0, "wit" : 0}
        
        #skills
        self.skills = {"animalhandling" : 0, "artistry" : 0, "biology" : 0, 
        "enchanting" : 0, "force" : 0, "illusion" : 0, "spatial" : 0, 
        "bruteforce" : 0, "cold" : 0, "fire" : 0, "lightning" : 0, 
        "necrosis" : 0, "rez" : 0, "deception" : 0, "exploration" : 0, 
        "freerunning" : 0, "judgement" : 0, "air" : 0, "earth" : 0, 
        "health" : 0, "nature" : 0, "water" : 0, "lockpicking" : 0, 
        "perform" : 0, "poisonresist" : 0, "search" : 0, "speechcraft" : 0, 
        "stamina" : 0, "streetsmarts" : 0, "wilderness" : 0}
        
        #Max values
        self.max = {"hp" : 25, "recovery" : 2, "weight" : 50, "ms" : 0}
        
        #Current values
        self.curr = {"hp" : 25, "recovery" : 2, "weight" : 50, "ms" : 0, 
        "overheal" : 0, "x" : 0, "y" : 0, "z" : 0, "tired":False}

        #Wearables and Weapons
        self.equipped = { "body" : None, "head" : None, "rring" : None, 
        "lring" : None, "rhand" : None, "lhand" : None, "neck" : None, 
        "feet" : None, "larm" : None, "rarm" : None}
        self.bags = { "back" : None, "waist1" : None, "waist2" : None}
        
        #Traits, Training and Perks
        self.traits = []
        self.training = []
        self.perks = []
        
        #Items
        self.gold = 0
        self.items = []
        
        #Magic
        self.magic = []
        
        #Flavor
        self.flavor = { "name" : "player", "age" : 18, "alignment" : "neutral", "backstory" : "none", "sex" : "male"}

#Definitions
#===========================================================
    #equip an item
    def equip(self, slot, item):
        if item not in self.items:
            return "Item not owned."
        elif slot not in self.equipped:
            return "Slot doesn't exist."
        else:
            self.equipped[slot] = item
    
    #update stats 
    #TODO add skills
    def updateStat(self, newStat, inc):
        if newStat not in self.stats:
            return "Not a valid stat."
        else:
            self.stats[newStat] = self.stats[newStat] + inc
            msrecalc = False
            if newStat is "cha":
                self.stats["cha"] += inc
            elif newStat is "dm":
                self.stats["dm"] += inc
                msrecalc = True
            elif newStat is "dex":
                self.stats["dex"] += inc
                self.main["dodge"] += inc
                self.main["speed"] += inc
            elif newStat is "hea":
                self.stats["hea"] += inc
                self.max["recovery"] += inc
                self.max["hp"] += (3 * inc)
            elif newStat is "lm":
                self.stats["lm"] += inc
                msrecalc = True
            elif newStat is "str":
                self.stats["str"] += inc
                self.max["weight"] += (10 * inc)
                mbase += newstat
            elif newStat is "sur":
                self.stats["sur"] += inc
            elif newStat is "wit":
                self.stats["wit"] += inc
                msrecalc = True
            #Sets magic stamina
            if msrecalc is True:
                tempmax = self.stats["lm"]
                if tempmax < self.stats["dm"]:
                    tempmax = self.stats["dm"]
                if tempmax < self.stats["wit"]:
                    tempmax = self.stats["wit"]
                self.max["ms"] = (3 * tempmax)

    #set race
    def setRace(self):
        pass
    
    #set class
    def setClass(self):
        update = classList.get(self.clss)
        for i in range(update[0]):
            getItem(update[0][i])
        self.gold = update[1]
        for i in range(update[2]):
            getTraining(update[2][i])
        for i in range(update[3]):
            getPerk(update[3][i])
        
    #get item
    def getItem(self, itemName, quan = 1):
        for i in range(quan):
            self.items.append(itemList.get(itemName))
        
    #remove item
    def removeItem(self, item, quan = 1):
        for i in range(quan):
            if item in self.items:
                self.items.remove(item)
            else:
                return "Could not remove all items"
        
    #get/remove training
    
    #get/remove perks
    
    #Test perks
    
    #Attack
    def attack(self, weapon, distance, targetlist):
        for i in targetlist:
            roll = random.randint(1,20)
            tohit = roll + weapon.attr["acc"] + self.stats["dex"]
            if tohit > targetlist[i].main["dodge"]:
                roll = weapon.attr["#ofdie"] * (random.randint(1,weapon.attr["die"]))
                roll -= targetlist[i].main["armor"]
                targetlist[i].main["hp"] -= roll
            else:
                return "miss"
