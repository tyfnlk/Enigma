import Enigma

enigma = Enigma.enigma()
enigma.plugBoard.swap("h", 'E')
print(enigma.plugBoard.board.items())
enigma.encrypt("hello")

