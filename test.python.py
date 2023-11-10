import Enigma

test = Enigma.enigma()
# testlist = test.strToInt("hello world")
# print(testlist)
# print(test.listToStr(testlist))
# print("--------------------")
# test.swap('E', 'L')

test.encrypt("Hello World")
print(test.rotor1.counter, test.rotor2.counter, test.rotor3.counter)

test.resetEnigma()
test.decrypt('HGNKZ TXNUF')



