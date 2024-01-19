from tkinter import *
import random

root = Tk()
root.title("Loot table")
root.geometry("400x400")


def loot_table(chest_size):
    window = Toplevel(root)
    window.geometry("400x300")
    window.title("Loot Output")
    Label(window, text ="You received: ").pack()
    text = Text(window, height = 10)
    if(chest_size == "s"):
        rolls = random.randint(2,3)
    elif(chest_size == "m"):
        rolls = random.randint(3,4)
    else:
        rolls = random.randint(5,7)
    
    for i in range(rolls):
        type_loot = random.randint(1,107)
        if(type_loot >= 1 and type_loot <=12):
            loot = Ingots()
            quantity = random.randint(1,4)
        elif(type_loot >= 13 and type_loot <= 29):
            loot = AlcIng()
            quantity = random.randint(1,3)
        elif(type_loot >= 30 and type_loot <= 39):
            loot = RCN()
            quantity = 1
        elif(type_loot >= 40 and type_loot <50):
            loot = WandA(chest_size)
            quantity = 1
        elif(type_loot >= 51 and type_loot <= 52):
            loot = Arrows()
            quantity = random.randint(3,12)
        elif(type_loot >= 53 and type_loot <= 62):
            loot = Tomes()
            quantity = 1
        elif(type_loot == 63):
            loot = Staff()
            quantity = 1
        elif(type_loot >= 64 and type_loot <= 75):
            loot = Soulgem()
            quantity = 1
        elif(type_loot >= 76 and type_loot <=80):
            loot = Gemstones()
            quantity = 1
        elif(type_loot >= 81 and type_loot <= 87):
            loot = Potion()
            quantity = 1
        else:
            loot = "Gold"
            if(chest_size == "s"):
                quantity = random.randint(7,25)
            elif(chest_size == "m"):
                quantity = random.randint(20,150)
            else:
                quantity = random.randint(100,300)
        output = "   " + loot + " with a quantity of " + str(quantity) + "\n"
        text.insert(1.0, output)     
    text.pack()
    text.configure(bg=window.cget('bg'), relief="flat")
    text.configure(state="disabled")   
    return loot, quantity

def OpenWindow():
    newWindow = Toplevel(root)
    newWindow.title("Chest Menu")
    b1_1 = Button(newWindow, text="Small Chest", padx=40, pady=20, command= lambda:loot_table("s"))
    b1_2 = Button(newWindow, text="Medium Chest", padx=40, pady=20, command= lambda:loot_table("m"))
    b1_3 = Button(newWindow, text="Large Chest", padx=40, pady=20, command= lambda:loot_table("l"))
    b1_1.grid()
    b1_2.grid()
    b1_3.grid()

def Ingots():
    num = random.randint(1,9)
    if(num == 1):
        output = "Iron Ingots"
    elif(num == 2):
        output = "Steel Ingots"
    elif(num == 3):
        output = "Dwarven Ingots"
    elif(num == 4):
        output = "Elven Ingots"
    elif(num == 5):
        output = "Orcish Ingots"
    elif(num == 6):
        output = "Malachite Ingots"
    elif(num == 7):
        output = "Silver Ingots"
    elif(num == 8):
        output = "Gold Ingots"
    else:
        output = "Ebony Ingots"
    return output

def Arrows():
    num = random.randint(1,8)
    if(num == 1):
        output = "Iron Arrows"
    elif(num == 2):
        output = "Steel Arrows"
    elif(num == 3):
        output = "Imperial Arrows"
    elif(num == 4):
        output = "Dwarven Arrows"
    elif(num == 5):
        output = "Elven Arrows"
    elif(num == 6):
        output = "Orcish Arrows"
    elif(num == 7):
        output = "Glass Arrows"
    else:
        output = "Ebony Arrows"
    return output

def RCN():
    num = random.randint(1,6)
    if(num == 1):
        output = "Silver Ring"
    elif(num == 2):
        output = "Gold Ring"
    elif(num == 3):
        output = "Silver Necklace"
    elif(num == 4):
        output = "Gold Necklace"
    elif(num == 5):
        output = "Silver Circlet"
    else:
        output = "Gold Circlet"
    return output
def AlcIng():
    num = random.randint(1,33)
    if(num == 1):
        output = "Bear Claws"
    elif(num == 2):
        output = "Troll Fat"
    elif(num == 3):
        output = "Spider Egg"
    elif(num == 4):
        output = "Ice Wraith Teeth"
    elif(num == 5):
        output = "Skeever Tail"
    elif(num == 6):
        output = "Spriggan Sap"
    elif(num == 7):
        output = "Hagraven Feathers"
    elif(num == 8):
        output = "Wisp Wrappings"
    elif(num == 9):
        output = "Dragon's Tongue"
    elif(num == 10):
        output = "Small Antlers"
    elif(num == 11):
        output = "Purple Mountain Flower"
    elif(num == 12):
        output = "Fire Salts"
    elif(num == 13):
        output = "Snowberries"
    elif(num == 14):
        output = "Void Salts"
    elif(num == 15):
        output = "Blue Dartwing"
    elif(num == 16):
        output = "Imp Stool"
    elif(num == 17):
        output = "Glow Dust"
    elif(num == 18):
        output = "Eye of Sabre Cat"
    elif(num == 19):
        output = "Vampire Dust"
    elif(num == 20):
        output = "Dwarven Oil"
    elif(num == 21):
        output = "Briar Heart"
    elif(num == 22):
        output = "Large Antlers"
    elif(num == 23):
        output = "Mammoth Tusk"
    elif(num == 24):
        output = "Mudcrab Chitin"
    elif(num == 25):
        output = "Frost Salts"
    elif(num == 26):
        output = "Salt Pile"
    elif(num == 27):
        output = "Juniper Berries"
    elif(num == 28):
        output = "Butterfly Wing"
    elif(num == 29):
        output = "Bone Meal"
    elif(num == 30):
        output = "Nirnroot"
    elif(num == 31):
        output = "Falmer Ear"
    elif(num == 32):
        output = "Hagraven Claw"
    elif(num == 33):
        output = "Giants Toe"
    return output

def WandA(chest_size):
    num = random.randint(1,7)
    screws = random.randint(1,100)
    if(num == 1):
        if(screws < 26):
            output = "Iron"
        elif(screws < 41):
            output = "Steel"
        elif(screws < 56):
            output = "Imperial"
        elif(screws < 71):
            output = "Dwarven"
        elif(screws < 81):
            output = "Elven"
        elif(screws < 91):
            output = "Orcish"
        elif(screws < 98):
            output = "Glass"
        else:
            output = "Ebony"
        bolt = random.randint(1,4)
        if(bolt == 1):
            output = output + " Sword"
        elif(bolt == 2):
            output = output + " Axe"
        elif(bolt == 3):
            output = output + " Warclub"
        else:
            output = output + " Dagger"
    elif(num == 2):
        bolt = random.randint(1,4)
        if(bolt == 1):
            if(screws < 26):
                output = "Iron"
            elif(screws < 41):
                output = "Steel"
            elif(screws < 56):
                output = "Imperial"
            elif(screws < 71):
                output = "Dwarven"
            elif(screws < 81):
                output = "Elven"
            elif(screws < 91):
                output = "Orcish"
            elif(screws < 98):
                output = "Glass"
            else:
                output = "Ebony"
            output = output + " Longsword"
        elif(bolt == 2):
            if(screws < 26):
                output = "Iron"
            elif(screws < 41):
                output = "Steel"
            elif(screws < 56):
                output = "Imperial"
            elif(screws < 71):
                output = "Dwarven"
            elif(screws < 81):
                output = "Elven"
            elif(screws < 91):
                output = "Orcish"
            elif(screws < 98):
                output = "Glass"
            else:
                output = "Ebony"
            output = output + " Greataxe"
        elif(bolt == 3):
            if(screws < 26):
                output = "Iron"
            elif(screws < 41):
                output = "Steel"
            elif(screws < 56):
                output = "Imperial"
            elif(screws < 71):
                output = "Dwarven"
            elif(screws < 81):
                output = "Elven"
            elif(screws < 91):
                output = "Orcish"
            elif(screws < 98):
                output = "Glass"
            else:
                output = "Ebony"
            output = output + " Warhammer"
        else:
            if(screws < 21):
                output = "Long"
            elif(screws < 41):
                output = "Hunting"
            elif(screws < 56):
                output = "Imperial"
            elif(screws < 71):
                output = "Dwarven"
            elif(screws < 81):
                output = "Elven"
            elif(screws < 91):
                output = "Orcish"
            elif(screws < 98):
                output = "Glass"
            else:
                output = "Ebony"
            output = output + " Bow"
    elif(num == 3):
        if(screws < 21):
            output = "Leather"
        elif(screws < 36):
            output = "Iron"
        elif(screws < 51):
            output = "Steel"
        elif(screws < 66):
            output = "Imperial"
        elif(screws < 76):
            output = "Dwarven"
        elif(screws < 84):
            output = "Elven"
        elif(screws < 91):
            output = "Orcish"
        elif(screws < 98):
            output = "Glass"
        else:
            output = "Ebony"
        output = output + " Shield"
    elif(num == 4):
        if(screws < 21):
            output = "Leather"
        elif(screws < 36):
            output = "Iron"
        elif(screws < 51):
            output = "Steel"
        elif(screws < 66):
            output = "Imperial"
        elif(screws < 76):
            output = "Dwarven"
        elif(screws < 84):
            output = "Elven"
        elif(screws < 91):
            output = "Orcish"
        elif(screws < 98):
            output = "Glass"
        else:
            output = "Ebony"
        output = output + " Gauntlets"
    elif(num == 5):
        if(screws < 21):
            output = "Leather"
        elif(screws < 36):
            output = "Iron"
        elif(screws < 51):
            output = "Steel"
        elif(screws < 66):
            output = "Imperial"
        elif(screws < 76):
            output = "Dwarven"
        elif(screws < 84):
            output = "Elven"
        elif(screws < 91):
            output = "Orcish"
        elif(screws < 98):
            output = "Glass"
        else:
            output = "Ebony"
        output = output + " Boots"
    elif(num == 6):
        if(screws < 21):
            output = "Leather"
        elif(screws < 36):
            output = "Iron"
        elif(screws < 51):
            output = "Steel"
        elif(screws < 66):
            output = "Imperial"
        elif(screws < 76):
            output = "Dwarven"
        elif(screws < 84):
            output = "Elven"
        elif(screws < 91):
            output = "Orcish"
        elif(screws < 98):
            output = "Glass"
        else:
            output = "Ebony"
        output = output + " Armor"
    else:
        if(screws < 21):
            output = "Leather"
        elif(screws < 36):
            output = "Iron"
        elif(screws < 51):
            output = "Steel"
        elif(screws < 66):
            output = "Imperial"
        elif(screws < 76):
            output = "Dwarven"
        elif(screws < 84):
            output = "Elven"
        elif(screws < 91):
            output = "Orcish"
        elif(screws < 98):
            output = "Glass"
        else:
            output = "Ebony"
        output = output + " Helmet"
    if(chest_size == "s"):
        bolt = random.randint(1,10)
        if(bolt == 1):
            output = "Enchanted " + output
    elif(chest_size == "m"):
        bolt = random.randint(1,5)
        if(bolt <= 2):
            output = "Enchanted " + output
    elif(chest_size == "l"):
        bolt = random.randint(1,2)
        if(bolt == 1):
            output = "Enchanted " + output
    return output

def Gemstones():
    num = random.randint(1,6)
    if(num == 1):        
        output = "Garnet"
    elif(num == 2):
        output = "Amethyst"
    elif(num == 3):
        output = "Ruby"
    elif(num == 4):
        output = "Sapphire"
    elif(num == 5):
        output = "Emerald"
    elif(num == 6):
        output = "Diamond"
    bolt = random.randint(1,8)
    if(bolt == 1):
        output = "Flawless " + output
    return output

def Soulgem():
    num = random.randint(1,5)
    bolt = random.randint(1,10)
    if(num == 1):
        if(bolt <= 6):
            output = "Filled Petty Soul Gem"
        else:
            output = "Empty Petty Soul Gem"
    elif(num == 2):
        if(bolt <= 5):
            output = "Filled Lesser Soul Gem"
        else:
            output = "Empty Petty Soul Gem"
    elif(num == 3):
        if(bolt <= 4):
            output = "Filled Greater Soul Gem"
        else:
            output = "Empty Greater Soul Gem"
    elif(num == 4):
        if(bolt <= 3):
            output = "Filled Grand Soul Gem"
        else:
            output = "Empty Grand Soul Gem"
    else:
        if(bolt <= 3):
            output = "Filled Black Soul Gem"
        else:
            output = "Empty Black Soul Gem"
    return output

def Tomes():
    output = "Spell Tome: " + Spells()
    return output

def Staff():
    output = "Staff of " + Spells()
    return output

def Spells():
    num = random.randint(1,33)
    if(num == 1):
        output = "Fire"
    elif(num == 2):
        output = "Frostbite"
    elif(num == 3):
        output = "Sparks"
    elif(num == 4):
        output = "Firebolt"
    elif(num == 5):
        output = "Icespike"
    elif(num == 6):
        output = "Lightning Bolt"
    elif(num == 7):
        output = "Fireball"
    elif(num == 8):
        output = "Icy Spear"
    elif(num == 9):
        output = "Thunder Bolt"
    elif(num == 10):
        output = "Flame Cloak"
    elif(num == 11):
        output = "Ice Storm"
    elif(num == 12):
        output = "Chain Lightning"
    elif(num == 13):
        output = "Conjure Familiar"
    elif(num == 14):
        output = "Raise Zombie"
    elif(num == 15):
        output = "Soul Trap"
    elif(num == 16):
        output = "Conjure Flame Atronach"
    elif(num == 17):
        output = "Reanimate Corpse"
    elif(num == 18):
        output = "Conjure Frost Atronach"
    elif(num == 19):
        output = "Revenant"
    elif(num == 20):
        output = "Conjure Storm Atronach"
    elif(num == 21):
        output = "Dread Zombie"
    elif(num == 22):
        output = "Courage"
    elif(num == 23):
        output = "Fury"
    elif(num == 24):
        output = "Calm"
    elif(num == 25):
        output = "Fear"
    elif(num == 26):
        output = "Muffle"
    elif(num == 27):
        output = "Rally"
    elif(num == 28):
        output = "Frenzy"
    elif(num == 29):
        output = "Invisibility"
    elif(num == 30):
        output = "Call To Arms"
    elif(num == 31):
        output = "Mayhem"
    elif(num == 32):
        output = "Oakflesh"
    elif(num == 33):
        output = "Candelight"
    elif(num == 34):
        output = "Equilibrium"
    elif(num == 35):
        output = "Stone Flesh"
    elif(num == 36):
        output = "Magelight"
    elif(num == 37):
        output = "Detect Life"
    elif(num == 38):
        output = "Iron Flesh"
    elif(num == 39):
        output = "Telekinesis"
    elif(num == 40):
        output = "Detect Dead"
    elif(num == 41):
        output = "Ebonyflesh"
    elif(num == 42):
        output = "Transmute"
    elif(num == 43):
        output = "Paralyze"
    elif(num == 44):
        output = "Healing"
    elif(num == 45):
        output = "Lesser Ward"
    elif(num == 46):
        output = "Sun Fire"
    elif(num == 47):
        output = "Fast Healing"
    elif(num == 48):
        output = "Steadfast Ward"
    elif(num == 49):
        output = "Necronmantic Healing"
    elif(num == 50):
        output = "Close Wounds"
    elif(num == 51):
        output = "Greater Ward"
    elif(num == 52):
        output = "Grand Healing"
    else:
        output = "Bane of the Undead"
    return output

def Potion():
    num = random.randint(1,7)
    if(num > 0 and num <= 2):
        bolt = random.randint(1,11)
        if(bolt == 1):
            output = "the Warrior"
        elif(bolt == 2):
            output = "the Berserker"
        elif(bolt == 3):
            output = "True Shot"
        elif(bolt == 4):
            output = "the Knight"
        elif(bolt == 5):
            output = "the Skirmisher"
        elif(bolt == 6):
            output = "Alteration"
        elif(bolt == 7):
            output = "Conjuration"
        elif(bolt == 8):
            output = "Restoration"
        elif(bolt == 9):
            output = "Illusion"
        elif(bolt == 10):
            output = "Destruction"
        else:
            output = "Light Feet"
        lvl = random.randint(2,5)
        output = "Potion of " + output + " Tier: " + str(lvl)
        return output
    elif(num > 2 and num <= 5):
        bolt = random.randint(1,8)
        if(bolt == 1):
            output = "Potion of Resist Fire " + str(random.randint(8,15))
        elif(bolt == 2):
            output = "Potion of Resist Frost " + str(random.randint(8,15))
        elif(bolt == 3):
            output = "Potion of Resist Shock " + str(random.randint(8,15))
        elif(bolt == 4):
            output = "Potion of Invisibility Time: " + str(random.choice([10,20,30]))
        elif(bolt == 5):
            output = "Potion of Healing Level: " + str(random.randint(1,3))
        elif(bolt == 6):
            output = "Potion of Magicka Tier " + str(random.randint(1,3))
        elif(bolt == 7):
            output = "Potion of Stamina Tier " + str(random.randint(1,3))
        else:
            output = "Potion of Cure Disease"
        return output
    else:
        bolt = random.randint(1,8)
        if(bolt == 1):
            output = "Healing Poison Level: " + str(random.randint(1,3))
        elif(bolt == 2):
            output = "Magicka Poison Tier: " + str(random.randint(1,3))
        elif(bolt == 3):
            output = "Stamina Poison Tier: " + str(random.randint(1,3))
        elif(bolt == 4):
            output = "Paralysis Poison Tier: " + str(random.randint(1,3))
        elif(bolt == 5):
            output = "Aversion to Fire " + str(random.randint(8,15))
        elif(bolt == 6):
            output = "Aversion to Frost " + str(random.randint(8,15))
        else:
            output = "Aversion to Shock " + str(random.randint(8,15))
        return output

def blacksmith():
    window2 = Toplevel(root)
    window2.title("Blacksmith Shop")
    window2.geometry("400x300")
    Label(window2,  text= "The Blacksmith has an inventory of:").pack()
    text = Text(window2, height = 20)
    screws = []
    while(len(screws) < random.randint(8,12)):
        output = WandA("n")
        if output not in screws:
            screws.append(output)
    for i in screws:
        text.insert(1.0, i + " with a quantity of 1\n")
    screws = []
    while(len(screws) < random.randint(3,8)):
        output = Ingots()
        if output not in screws:
            screws.append(output)
    for i in screws:
        text.insert(1.0, i + " with a quantity of " + str(random.randint(3,10)) +  "\n")
    text.insert(1.0, "Leather with a quantity of " + str(random.randint(2,4)) + "\n")
    text.insert(1.0, "Leather Strips with a quantity of " + str(random.randint(3,8))+"\n")
    text.pack()
    text.configure(bg=window2.cget('bg'), relief="flat")
    text.configure(state="disabled")
def alchemy():
    window2 = Toplevel(root)
    window2.title("Alchemy Shop")
    Label(window2,  text= "The Alchemy Shop has an inventory of:").pack()
    text = Text(window2, height = 20)
    screws = []
    while(len(screws) < random.randint(8,20)):
        output = AlcIng()
        if output not in screws:
            screws.append(output)
    for i in screws:
        text.insert(1.0, i + " with a quantity of " + str(random.randint(5,10)) + "\n")
    screws = []
    while(len(screws) < random.randint(4,8)):
        output = Potion()
        if output not in screws:
            screws.append(output)
    for i in screws:
        text.insert(1.0, i + " with a quantity of " + str(random.randint(1,5)) + "\n")
    text.pack()
    text.configure(bg=window2.cget('bg'), relief="flat")
    text.configure(state="disabled")


def wizard():
    window2 = Toplevel(root)
    window2.title("Court Wizard Shop")
    Label(window2,  text= "The Court Wizard has an inventory of:").pack()
    text = Text(window2, height = 20)
    screws = []
    while(len(screws) < random.randint(2,3)):
        output = Soulgem()
        if output not in screws:
            screws.append(output)
    for i in screws:
        text.insert(1.0, i + " with a quantity of " + str(random.randint(1,3)) +  "\n")
    screws = []
    while(len(screws) < random.randint(3,7)):
        output = Tomes()
        if output not in screws:
            screws.append(output)
    for i in screws:
        text.insert(1.0, i + " with a quantity of " + str(random.randint(1,2)) + "\n")
    text.pack()
    text.configure(bg=window2.cget('bg'), relief="flat")
    text.configure(state="disabled")


b_1 = Button(root, text="Chest", padx=165, pady=36, command= lambda:OpenWindow())
b_2 = Button(root, text="Blacksmith", padx=140, pady=36, command= lambda:blacksmith())
b_3 = Button(root, text="Alchemy Shops", padx=130, pady=36, command= lambda:alchemy())
b_4 = Button(root, text="Court Wizard", padx=140, pady=36, command= lambda:wizard())




b_1.grid()
b_2.grid()
b_3.grid()
b_4.grid()


root.mainloop()