import string

import rotor
import PlugBoard
#generate rotor
class enigma:
    def __init__(self):
        self.plugBoard = PlugBoard.PlugBoard()
        #create 3 rotos
        self.rotor1 =rotor.rotor(0,0,0)
        self.rotor2 =rotor.rotor(0,0,1)
        self.rotor3 = rotor.rotor(0,0,2)

    def strToInt(self, msg: str):
        #convert string to character value (0-25)
        #x = space
        templist = []
        for i in range(len(msg)):
            x= ord(msg[i].upper()) -65

            if x == -33:
                templist.append('x')
            elif x<0 or x>25:
                pass
            else:
                templist.append(x)
        return templist

    def listToStr(self, list:[]):
        tempStr =""
        for i in range(len(list)):
            if list[i] == 'x':
                tempStr = tempStr + " "
            else:
                tempStr = tempStr + chr(list[i]+65)
        return tempStr


    def encrypt(self,letter:str):
        pass




test = enigma()
testlist = test.strToInt("hello world")
print(testlist)
print(test.listToStr(testlist))
