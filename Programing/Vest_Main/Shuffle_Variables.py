'''This Program Randomly Shuffles the variables'''

'''I copied from the original program with some simple modifications to make it more clear'''

'''The code below will create the neccessery variables
You can add some variables if you want or is needed'''

import random


'''The code for certain destinations of the ("minecraft") manhunt'''

Building_Letters = ("A", "B", "B2", "C", "E", "E2", "F", "G", "H1", "H", "K", "L", "M", "N", "N2", "P")

'''These are all the building letters that exist in Henry's Complex'''

All_Buildings = \
("A:32:1",
 "B:30:1", "B:31:1", "B:35:1", "B:36:1", "B:35:2", "B:36:2",
 "C:27:1", "C:28:1",
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
            "1":["32"]}, \
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

Numbers_Corresponding_To_Building_Letters = {"1":"A", "2":"B", "3":"C", "4":"E", "5":"F", "6":"G", "7":"H1", "8":"H", "9":"K", "10":"L", "11":"M", "12":"N", "13":"P"}
'''This way I can use the Random module to generate random building letters'''
Spawn_Letter = str(Numbers_Corresponding_To_Building_Letters[str(random.randint(1,12))])
'''Write this down in a variable so that I can display it as well'''
Spawn_First_Or_Second_Building = str(random.randint(1,2))
'''Because there are so  many buildings in Henry's complex with the same letters, I have split it into either 1 or 2 this variable is randomly generated either 1 or 2'''
Spawn_Building_Number = 0

for key in All_Buildings_Dictionary:
    if Spawn_Letter == "A" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = "32"
        Spawn = All_Buildings[0]
        break
    if Spawn_Letter == "B" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number_With_Skips = str(random.randint(1, 2))
        if Spawn_Building_Number_With_Skips == "1":
            Spawn_Building_Number = str(random.randint(30, 31))
            if Spawn_Building_Number == "30":
                Spawn = All_Buildings[1]
                break
            if Spawn_Building_Number == "31":
                Spawn = All_Buildings[2]
                break
            break
        if Spawn_Building_Number_With_Skips == "2":
            Spawn_Building_Number = str(random.randint(35, 36))
            if Spawn_Building_Number == "35":
                Spawn = All_Buildings[3]
                break
            if Spawn_Building_Number == "36":
                Spawn = All_Buildings[4]
                break
            break
        break
    if Spawn_Letter == "B" and Spawn_First_Or_Second_Building == "2":
        Spawn_Building_Number = str(random.randint(35, 36))
        if Spawn_Building_Number == "35":
            Spawn = All_Buildings[5]
            break
        if Spawn_Building_Number == "36":
            Spawn = All_Buildings[6]
            break
        break
    if Spawn_Letter == "C" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.randint(27, 28))
        if Spawn_Building_Number == "27":
            Spawn = All_Buildings[7]
            break
        if Spawn_Building_Number == "28":
            Spawn = All_Buildings[8]
            break
        break
    if Spawn_Letter == "E" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.randint(26, 27))
        if Spawn_Building_Number == "26":
            Spawn = All_Buildings[9]
            break
        if Spawn_Building_Number == "27":
            Spawn = All_Buildings[10]
            break
        break
    if Spawn_Letter == "E" and Spawn_First_Or_Second_Building == "2":
        Spawn_Building_Number = str(random.randint(1, 2))
        if Spawn_Building_Number == "1":
            Spawn = All_Buildings[11]
            break
        if Spawn_Building_Number == "2":
            Spawn = All_Buildings[12]
            break
        break
    if Spawn_Letter == "F" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = "34"
        Spawn = All_Buildings[13]
        break
    if Spawn_Letter == "G" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = "29"
        Spawn = All_Buildings[14]
        break
    if Spawn_Letter == "H1" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.ranint(1, 3))
        if Spawn_Building_Number == "1":
            Spawn = All_Buildings[15]
            break
        if Spawn_Building_Number == "2":
            Spawn = All_Buildings[16]
            break
        if Spawn_Building_Number == "3":
            Spawn = All_Buildings[17]
            break
        break
    if Spawn_Letter == "H" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.ranint(6, 7))
        if Spawn_Building_Number == "6":
            Spawn = All_Buildings[18]
            break
        if Spawn_Building_Number == "7":
            Spawn = All_Buildings[19]
            break
        break
    if Spawn_Letter == "K" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.randint(1, 7))
        if Spawn_Building_Number == "1":
            Spawn = All_Buildings[20]
            break
        if Spawn_Building_Number == "2":
            Spawn = All_Buildings[21]
            break
        if Spawn_Building_Number == "3":
            Spawn = All_Buildings[22]
            break
        if Spawn_Building_Number == "4":
            Spawn = All_Buildings[23]
            break
        if Spawn_Building_Number == "5":
            Spawn = All_Buildings[24]
            break
        if Spawn_Building_Number == "6":
            Spawn = All_Buildings[25]
            break
        if Spawn_Building_Number == "7":
            Spawn = All_Buildings[26]
            break
        break
    if Spawn_Letter == "L" and Spawn_First_Or_Second_Building == "1":
        Spawn = All_Buildings[27]
        Spawn_Building_Number = "1"
        break
    if Spawn_Letter == "M" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.randin(1, 2))
        if Spawn_Building_Number == "1":
            Spawn = All_Buildings[28]
            break
        if Spawn_Building_Number == "2":
            Spawn = All_Buildings[29]
            break
        break
    if Spawn_Letter == "N" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.randin(1, 2))
        if Spawn_Building_Number == "1":
            Spawn = All_Buildings[30]
            break
        if Spawn_Building_Number == "2":
            Spawn = All_Buildings[31]
            break
        break
    if Spawn_Letter == "N" and Spawn_First_Or_Second_Building == "2":
        Spawn_Building_Number = str(random.randin(1, 2))
        if Spawn_Building_Number == "1":
            Spawn = All_Buildings[32]
            break
        if Spawn_Building_Number == "2":
            Spawn = All_Buildings[33]
            break
        break
    if Spawn_Letter == "P" and Spawn_First_Or_Second_Building == "1":
        Spawn_Building_Number = str(random.randint(1, 11)
        if Spawn_Building_Number == "1":
            Spawn = All_Buildings[34]
            break
        if Spawn_Building_Number == "2":
            Spawn = All_Buildings[35]
            break
        if Spawn_Building_Number == "3":
            Spawn = All_Buildings[36]
            break
        if Spawn_Building_Number == "4":
            Spawn = All_Buildings[37]
            break
        if Spawn_Building_Number == "5":
            Spawn = All_Buildings[38]
            break
        if Spawn_Building_Number == "6":
            Spawn = All_Buildings[39]
            break
        if Spawn_Building_Number == "7":
            Spawn = All_Buildings[40]
            break
        if Spawn_Building_Number == "8":
            Spawn = All_Buildings[41]
            break
        if Spawn_Building_Number == "9":
            Spawn = All_Buildings[42]
            break
        if Spawn_Building_Number == "10":
            Spawn = All_Buildings[43]
            break
        if Spawn_Building_Number == "11":
            Spawn = All_Buildings[44]
            break
        break
    break
break
print('Spawn Letter: "', str(Spawn_Letter), '", First Or Second Building: "', str(Spawn_First_Or_Second_Building), '" ', "Building Number: ", str(Spawn_Building_Number), sep="")
