import Enigma
import flet as ft

def main(page: ft.page):
    pass






test = Enigma.enigma()
testlist = test.strToInt("hello world")
print(testlist)
print(test.listToStr(testlist))
print("--------------------")
test.swap('E', 'L')
test.encrypt("I like to eat cheese")
