#create rotor object
class rotor:
    #constructor function
    # initiate the start and advance cog
    def __init__(self,  start: int, trigger: int, type: int):
        self.start = start
        self.trigger = trigger
        self.type = type
        self.counter = start
        self.rotor = None
        self.rotor0 = {
            0: 15,
            1: 17,
            2: 20,
            3: 19,
            4: 4,
            5: 25,
            6: 10,
            7: 13,
            8: 18,
            9: 16,
            10: 8,
            11: 5,
            12: 21,
            13: 9,
            14: 0,
            15: 11,
            16: 6,
            17: 24,
            18: 23,
            19: 1,
            20: 2,
            21: 7,
            22: 14,
            23: 3,
            24: 22,
            25: 12
        }
        self.rotor1 = {
            0: 18,
            1: 21,
            2: 11,
            3: 16,
            4: 25,
            5: 5,
            6: 6,
            7: 2,
            8: 13,
            9: 1,
            10: 22,
            11: 7,
            12: 15,
            13: 14,
            14: 4,
            15: 17,
            16: 12,
            17: 24,
            18: 20,
            19: 9,
            20: 23,
            21: 0,
            22: 8,
            23: 19,
            24: 10,
            25: 3

        }
        self.rotor2 = {
            0: 12,
            1: 16,
            2: 23,
            3: 0,
            4: 4,
            5: 14,
            6: 17,
            7: 22,
            8: 25,
            9: 10,
            10: 24,
            11: 1,
            12: 7,
            13: 9,
            14: 11,
            15: 19,
            16: 5,
            17: 15,
            18: 8,
            19: 13,
            20: 18,
            21: 20,
            22: 2,
            23: 3,
            24: 6,
            25: 21

        }



    def setStart(self, start: int): #set the starting position of rotor
        if start >=0 and start <=25:
            self.start =start
        else:
            self.start=0
        return self.start()

    def getStart(self): #get the starting position of the rotor
        return self.star

    def setTrigger(self, advance:int): # set the point where the cog will advance rotor aheaed
        if advance >=0  and advance <=25:
            self.trigger= advance
        else:
            self.trigger=0
        return self.trigger()

    def getTrigger(self): # get point where cog will advance rotor ahead
        return self.trigger

    def setType(self, type: int):
        self.type = type


    def passRotor(self, value:int): # pass value through selected rotor
        if self.type ==0:
            return self.rotor0.get(value)
        elif self.type ==1:
            return self.rotor1.get(value)
        elif self.type == 2:
            return self.rotor2.get(value)

    def advance(self):  # rotate the rotor one click
        self.counter= self.counter +1
        if self.counter ==26:
            self.counter ==0

    def checkTrigger(self): #check if trigger is advanced
        if self.counter == self.trigger()
            return True
        return False
    def print(self):
        print('start is ', self.start, 'advance is ', self.trigger, 'type is', self.type)

    def convert(self, value: int): #input value to rotor, and return conversion
        print('value is', value)
        if value > 25 or value< 0:
            print("fail convert")
            pass
        else:
            print('pass')
            #get value based upon rotor placement
            temp = (value + self.start) % 26
            print(temp)

            #get coversion by rotor
            temp = self.passRotor(temp)
            print(value, 'is now', temp)
            #return value with key = temp
            #advance count



