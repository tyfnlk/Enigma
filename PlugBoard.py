
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


