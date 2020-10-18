# Hangman.py
# 2020/08/28
# Fjfjaonfsldfn, requested
# Let's have fun and make a hangman
class Hangman():
    def __init__(self, word):
        self.word = word
        self.guess = ""
        self.mistakes = 0
        self.wrongLetters = []
        for i in word:
            if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
               self.guess = self.guess + '-'
            else:
                self.guess = self.guess + i

    def returnGuess(self):
        hang = ""
        if self.mistakes == 0:
            hang = " ___\n|  |\n|\n|\n|\n____"
        elif self.mistakes == 1:
            hang = " ___\n|  |\n|  O\n|\n|\n____"
        elif self.mistakes == 2:
            hang = " ___\n|  |\n|  O\n|  |\n|\n____"
        elif self.mistakes == 3:
            hang = " ___\n|  |\n|  O\n| /|\n|\n____"
        elif self.mistakes == 4:
            hang = " ___\n|  |\n|  O\n| /|\ \n|\n____"
        elif self.mistakes == 5:
            hang = " ___\n|  |\n|  O\n| /|\ \n| /\n____"
        elif self.mistakes == 6:
            hang = " ___\n|  |\n|  O\n| /|\ \n| / \ \n____"
        wl = ""
        for i in self.wrongLetters:
            wl = wl + i
        return "Word: " + self.guess + "\n```" + hang + "```\n" "Wrong letters: " + wl
    
    def checkWin(self):
        if self.guess == self.word:
            return True
        return False
    
    def checkLoss(self):
        if self.mistakes > 5:
            return True
        return False

    def containsLetter(self, letter):
        return letter.lower() in self.word.lower()

    def addMistake(self, letter):
        if not letter in self.wrongLetters:
            self.mistakes = self.mistakes + 1
            self.wrongLetters.append(letter)

    def replace(self, letter):
        let = letter.lower()
        temp = list(self.guess)
        for i in range(len(self.word)):
            if self.word[i].lower() == let:
                temp[i] = self.word[i]
        self.guess = ""
        for i in temp:
            self.guess = self.guess + i

    def guessLetter(self, letter):
        if self.containsLetter(letter):
            self.replace(letter)
        else:
            self.addMistake(letter)
