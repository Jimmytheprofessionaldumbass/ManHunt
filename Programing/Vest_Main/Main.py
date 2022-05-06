'''The Main Program'''


'''Starting up and importing modules'''

print("Starting")

'''This indicates to the user that the program/code 
is running and (hopefully) working'''

import time
'''This imports time module'''
time.sleep(0.5)
'''This adds a delay so the user notices'''
print("Starting.")
'''This indicates that the program has entered 
the second stage of starting up'''

import random
'''This imports the random module 
(You can add more modules if it is needed)'''
time.sleep(0.05)
print("Starting..")

import cv2 as cv
'''This Imports the OpenCV Module for Computer Vision'''
time.sleep(0.05)
print("Starting...")

time.sleep(0.05)
print("Finished Loading.")
'''This tells the user that the program 
has finished loading modules'''


'''Create Variables'''

'''The code below will create the neccessery variables
You can add some variables if you want or is needed'''


'''The code for certain destinations of the ("minecraft") manhunt'''

Building_Letters = ("A", "B", "B2", "C", "E", "E2", "F", "G", "H1", "H", "K", "L", "M", "N", "N2", "P")

'''These are all the building letters that exist in Henry's Complex'''

All_Buildings = \
("A:32:1",
 "B:30:1", "B:31:1", "B:35:1", "B:36:1", "B:35:2", "B:36:2",
 "C:27", "C:28",
 "E:26:1", "E:27:1",
 "E:1:2", "E:2:2",
 "F:34:1",
 "G:29:1",
 "H1:1:1", "H1:2:1", "H1:3:1",
 "H:6:1", "H:7:1",
 "K:1:1", "K:2:1", "K:3:1", "K:4:1", "K:5:1", "K:6:1", "K:7:1",
 "L:1:1",
 "M:1:1", "M:2:1",
 "N:1:1", "N:2:1",
 "N:1:2", "N:2:2",
 "P:1:1", "P:2:1", "P:3:1", "P:4:1", "P:5:1",
 "P:6:1", "P:7:1", "P:8:1", "P:9:1", "P:10:1", "P:11:1")

All_Buildings_Dictionary = {\
        "A":{\
            "1":[32]}, \
        "B":{\
            "1":["30", "31", "35", "36"], \
            "2":["35", "36"]}, \
        "C":{\
            "1":["27", "28"]}, \
        "E":{\
            "1":["26", "27"], \
            "2":["1", "2"]}, \
        "F":{\
            "1":["34"]}, \
        "G":{\
            "1":["29"]}, \
        "H1":{\
            "1":["1", "2", "3"]}, \
        "H":{\
            "1":["6", "7"]}, \
        "K":{\
            "1":["1", "2", "3", "4", "5", "6", "7"]}, \
        "L":{\
            "1":["1"]}, \
        "M":{\
            "1":["1", "2"]}, \
        "N":{\
            "1":["1", "2"], \
            "2":["1", "2"]}, \
        "P":{\
            "1":["1", "2", "3", "4", "5", "6", "7"]}}



Underground_Letters = []

'''This is all the Letters of the underground parking lot.'''

Underground_Numbers = []

'''This gives the computer a better advantage of how to better sense where 
the other objects (Blaze rods) are.'''

Spawn = None

'''This is where the playeruser starts the 
speed run, it is usually a building, 
 a building has a letter and a number, the spawn 
 area specifically can be 
not chosen, chosen smartly or chosen randomly'''

Time_Of_Nether_Portal_Spawn = None
'''variable that determines the time till the nether portal spawns'''

'''This is the amount of time that the player 
has to survive before the Nether Portal
Spawns, if the Player didn't manage to survive in this 
amount of time, the game ends or the
play has lost, the time is 2 to 5 minutes'''

Nether_Portal_First_Letter = None

'''This is the first letter of the location of the nether portal, 
every player needs to go through this building in 
order to continue to hunt down the speedrunner '''

Nether_Portal_First_Number = None

'''This is the first number of the location of the nether portal, 
every player needs to go through this building in 
order to continue to hunt down the speedrunner '''

Nether_Portal = None

'''This is the building where all the players 
(including the manhunters) have to go through 
in order to continue the game.
the building name is created by combining two 
values together to create the random building'''

'''To indicate whether the speedrunner has gone 
through the nether portal, there will be a device in the gates 
of the elevator, hidden to not be caught by normal people and stolen
there will be a device in ever building because the Nether Portals 
are going to be chosen randomly'''

Nether_Fortress = None

'''This is the area where there is blaze rods, which is required to 
access the end portal, it gives only a letter and the blaze rods will
be nowhere out of that area. When the sensors of the Raspberry pi on the 
speedrunner detects the 12 blaze rods it will give the speedrunner the 
compass navigation (similar to minecraft compasses) but it refreshes 
when the player inputs it to the Raspberry Pi like how eyes of ender work.'''

# More about blaze rods and how they work.
'''This is the place where the blaze rods are found, aka an small 
electronic device, that indicates if the blaze rod is found when
pressed a button on it, the speedrunner needs to collect a total of 
12 blaze rods hidden in the parking lot, at the end of the game, they
will be picked up using location and bluetooth and sound. There are 
going to be 12 blaze rods not in every part of the parking lot
otherwise, it would first, cost a lot of money, or secondly, 
another blaze rod that was in another area of the parking lot, be
taken by the speedrunner which isn't supposed to happen. 
The Nether Fortresses are going to be very far away from each other
to prevent getting take by a closer place. The blaze rods will be hidden,
but will be more like the eyes of ender, you can tell the Raspberry Pi 
show the directions like a compass but it can only be used 36 times 
to tell the directions, 3 times per rod. If all of the chances to 
tell the location the speedrunner may either, give up on life, or keep 
on finding it with bare eyes. '''

StrongHold = None

'''This is the most important part of the game, and the most complex, 
The speedrunner has to both escape from being killed by the hunters 
and also find the stronghold, there will be devices like the ones in the
Nether portal to indicate, like the nether portal, the device will be also 
put into every building or for the cheaper choice, it can be instead just 
be the Nether Portal sensor but with more code. The program will specify the
building letter, but won't tell the numbers, the speedrunner then has to 
go through all of the buildings with that letter and then there is going 
to be a status bar showing how close the speerunner is to the portal,
this feature of showing how close (or hot) he is to the end can be removed'''
