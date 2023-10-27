import string

import rotor
import PlugBoard
#generate rotor
class enigma:
    def __init__(self):
        self.plugBoard = PlugBoard.PlugBoard()
        #create 3 rotos
        self.rotor1 =rotor.rotor(0,25,0)
        self.rotor2 =rotor.rotor(0,25,1)
        self.rotor3 = rotor.rotor(0,25,2)

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

    def swap(self, x: int, y: int):
       return self.plugBoard.swap(x,y)

    def swap(self, x: str, y: str):
        return self.plugBoard.swap(x,y)

    def resetPlugboard(self):
        return self.plugBoard.reset()

    def resetEnigma(self):
        self.rotor1.reset()
        self.rotor2.reset()
        self.rotor3.reset()

    def encrypt(self,msg:str):
        #convert string to list
        print("string is:", msg)
        msgList = self.strToInt(msg)
        print("converted to ints:", msgList)

        #pass list through plug board
        msgList = self.plugBoard.passPlugBoard((msgList))
        print("after plugboard:", msgList)

        #pass each letter through the rotors 1,2,3,3,2,1

        for i in range(len(msgList)):
            if msgList[i] == 'x':
                pass
            else:
                temp = msgList[i]
                temp = self.rotor1.passRotor(temp)
                temp = self.rotor2.passRotor(temp)
                temp = self.rotor3.passRotor(temp)
                temp = self.rotor3.passRotor(temp)
                temp = self.rotor2.passRotor(temp)
                temp = self.rotor1.passRotor(temp)

                msgList[i] = temp

                # advance rotor
                self.incrementRotor()

        #pass through plug board
        msgList = self.plugBoard.passPlugBoard((msgList))
        print("after plugboard:", msgList)

        #return string
        msg = self.listToStr(msgList)
        print("ecryption is:", msg)
        return msg


        pass

    def incrementRotor(self):
        self.rotor1.advance()
        print("rotor 1 advance")
        if self.rotor1.checkTrigger() == True:
            self.rotor2.advance()
            print("rotor 2 advance")
            if self.rotor2.checkTrigger() == True:
                self.rotor3.advance()
                print("rotor 3 advance")

    def decrypt(self,msg:str):
        #convert string to list
        print("string is:", msg)
        msgList = self.strToInt(msg)
        print("converted to ints:", msgList)

        #pass list through plug board
        msgList = self.plugBoard.passPlugBoard((msgList))
        print("after plugboard:", msgList)

        #pass each letter through the rotors 1,2,3,3,2,1

        for i in range(len(msgList)):
            if msgList[i] == 'x':
                pass
            else:
                temp = msgList[i]
                temp = self.rotor1.reversePass(temp)
                temp = self.rotor2.reversePass(temp)
                temp = self.rotor3.reversePass(temp)
                temp = self.rotor3.reversePass(temp)
                temp = self.rotor2.reversePass(temp)
                temp = self.rotor1.reversePass(temp)

                msgList[i] = temp

                # advance rotor
                self.rotor1.advance()
                print("rotor 1 advance")
                if self.rotor1.checkTrigger() == True:
                    self.rotor2.advance()
                    print("rotor 2 advance")
                    if self.rotor2.checkTrigger() == True:
                        self.rotor3.advance()
                        print("rotor 3 advance")



        #return string
        msg = self.listToStr(msgList)
        print("decryption is:", msg)
        return msg


        pass

