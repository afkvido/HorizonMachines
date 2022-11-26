# Credit to JP#3356 on Discord

from ast import Break, match_case
from http.client import CONTINUE
import inspect
from platform import machine
from random import choices, randint, randrange, sample
import random
from secrets import choice
from time import sleep
import textwrap
from textwrap import fill

# Main Interface
input("Welcome to the Horizon random machine name generator!")
print("Here you will be able to create a machine name depending on the core features of your machine")
print("-----------------------")
print("Select the theme of your machine.")
print("(F)ire Based, (Fr)ost based, (E)lectricity based, (Ea)rth based, (A)cid based machine, (K)iller Machine")
UserInput = input(": ")
print("-----------------------")

# Name sections
fireNames = ['flame', 'ember', 'fire', 'burn', 'torch']
frostNames = ['freeze', 'frost']
electricityNames = ['storm', 'shock', 'electro', 'thunder', 'breaker']
earthNames = ['rock', 'breaker', 'jaw', 'stone', 'cutter', 'saw', 'ripper']
acidNames = ['acid', 'burn']
killerNames = ['jaw', 'slaughter', 'breaker', 'spine', 'thunder', 'claw', 'saw', 'tooth']

flyingNames = ['Hawk', 'Phantom', 'bird', 'wing', 'wind']
waterNames = ['tide', 'maw', 'snap', 'surf']
landNames = ['jaw', 'lasher', 'strider', 'saw', 'breaker']

# Boleeans
fireChosen = False
frostChosen = False
electricityChosen = False
earthChosen = False
acidChosen = False
killerChosen = False
flyingChosen = False
LandChosen = False
waterChosen = False

prompt1 = ""
prompt2 = ""

# Elemental prompts
firePrompt = "fire"
frostPrompt = "frost"
electricityPrompt = "electric"
earthPrompt = "earth"
acidPrompt = "acid"
killerPrompt = "killer"

flyingPrompt = "flying"
waterPrompt = "aquatic"
landPrompt = "land"

# Logic Section 1 
if UserInput == ("F"):
    fireChosen = True
    prompt1 = firePrompt
if UserInput == ("Fr"):
    frostChosen = True
    prompt1 = frostPrompt
if UserInput == ("E"):
    electricityChosen = True
    prompt1 = electricityPrompt
if UserInput == ("Ea"):
    earthChosen = True
    prompt1 = earthPrompt
if UserInput == ("A"):
    acidChosen = True
    prompt1 = acidPrompt
if UserInput == ("K"):
    killerChosen = True
    prompt1 = killerPrompt

fireChosen = True
print("Please enter the class of the machine")
print("(F)lying, (W)ater, (L)and")
playerMachineClassInput = input("Enter your selection here: ")

if playerMachineClassInput == ("F"):
    flyingChosen = True
    prompt2 = flyingPrompt
if playerMachineClassInput == ("W"):
    waterChosen = True
    prompt2 = waterPrompt
if playerMachineClassInput == ("L"):
    landChosen = True
    prompt2 = landPrompt



print(f"{prompt1} {prompt2} based machine chosen")
sleep(1)
print("-----------------------")
print("Generating names...")

if prompt1 == firePrompt:
    nameSection1 = str(random.choice(fireNames))
if prompt1 == frostPrompt:
    nameSection1 = str(random.choice(frostNames))
if prompt1 == electricityPrompt:
    nameSection1 = str(random.choice(electricityNames))
if prompt1 == acidPrompt:
    nameSection1 = str(random.choice(acidNames))
if prompt1 == killerPrompt:
    nameSection1 = str(random.choice(killerNames))
if prompt1 == earthPrompt:
    nameSection1 = str(random.choice(earthNames))

if prompt2 == flyingPrompt:
    nameSection2 = str(random.choice(flyingNames))
if prompt2 == waterPrompt:
    nameSection2 = str(random.choice(waterNames))
if prompt2 == landPrompt:
    nameSection2 = str(random.choice(landNames))

randomOutput = ['1', '2']

nameOrder = str(random.choice(randomOutput))

if nameOrder == ("1"):
    print(f"The generated name you got is {nameSection1}{nameSection2}")
    print("-------------------------------------")

if nameOrder == ("2"):
    print(f"The generated name you got is {nameSection2}{nameSection1}")
    print("-------------------------------------")






