import discord

# Connect4.py
# 2020/08/29
# requested :D
# welp checkWin will be bothersome, let's go

class Connect4():
    def __init__(self, player1, player2, dark, p1, p2):
        self.player1 = player1
        self.player2 = player2
        self.dark = dark
        self.p1 = p1
        self.p2 = p2
        self.board = [
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']
        ]
        self.turn = 0

    def checWin(self, piece, x, y):
        ret = [True, True, True, True, True, True]
        for i in range(4):
            if (x + i < 7) and (not (self.board[x + i][y] == piece)):
                ret[0] = False
            elif (y + i < 6) and (not (self.board[x][y + 1] == piece)):
                ret[1] = False
            elif (x - i > -1) and (not (self.board[x - i][y] == piece)):
                ret[2] = False
            elif (y - i > -1) and (not (self.board[x][y - 1] == piece)):
                ret[3] = False
            elif (x + i < 7 and y + i < 6) and (not(self.board[x + i][y + i] == piece)):
                ret[4] = False
            elif (x - i > -1 and y - i > -1) and (not(self.board[x - i][y - i] == piece)):
                ret[5] = False
            
        return True in ret

    def getTurn(self):
        if self.turn%2==0:
            return 'r'
        else:
            return 'b'
        
    def move(self, row):
        for i in range(5, -1, -1):
            if self.board[i][row] == ' ':
                if self.turn %2 == 0:
                    self.board[i][row] = self.p1
                else:
                    self.board[i][row] = self.p2
                break
        self.turn += 1

    def be_string_lol(self):
        space = ":white_circle:"
        if self.dark:
            space = ":black_circle:"
        s = ""
        for i in self.board:
            for j in i:
                if j == " ":
                    s += space
                else:
                    s += j
            s += "\n"
        return s