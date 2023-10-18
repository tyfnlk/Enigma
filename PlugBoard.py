
class PlugBoard:
    def __init__(self):
        self.board = {}
        #auto insert all letters
        for i in range(26):
            self.board[i] =i
    def reset(self):
        #remove all plugs from plugboard
        for i in range(26):
            self.board[i] =i

    def swap(self, first:int, second: int):
        if self.board[first] == first and self.board[second] == second:
            self.board[first] = second
            self.board[second] = first
            return True
        else:
            return False

    def swap(self, first: str, second: str):
        if len(first) ==1 and len(second) ==1:
            first = ord(first[0].upper()) -65
            second = ord(second[0].upper()) -65
        if self.board[first] == first and self.board[second] == second:
            self.board[first] = second
            self.board[second] = first
            return True
        else:
            return False

    def passpb(self, x):
        if x =='x':
            return
        elif type(x) == int:
            return self.board[x]
    def passPlugBoard(self, msg:list):
        for i in range(len(msg)):
            if msg[i] == 'x':
                pass
            else:
                msg[i] = self.board[msg[i]]
        return msg


pb= PlugBoard()
pb.swap('a','b')
print(pb.board.items())

print(pb.passpb(1))