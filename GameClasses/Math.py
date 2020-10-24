# Math.py
# 2020/10/24
# Idk bro, procrastination
# Just gives math questions???
import random
class Math():
    def __init__(self):
        self.n1 = random.randrange(-100, 100)
        self.n2 = random.randrange(-100, 100)
        self.operator = None
        self.answer = None
        temp = random.random()
        if(temp < 0.25):
            self.operator = "+"
            self.answer = self.n1 + self.n2
        elif(temp < 0.5):
            self.operator = "-"
            self.answer = self.n1 - self.n2
        elif(temp < 0.75):
            self.operator = "*"
            self.answer = self.n1 * self.n2
        else:
            self.operator = "/"
            self.answer = self.n1 / self.n2
            while not(self.answer.is_integer()):
                self.n1 = random.randrange(100)
                self.n2 = random.randrange(100)
                self.answer = self.n1 / self.n2

    def __str__(self):
        return f"{self.n1} {self.operator} {self.n2} = ?"
    
    def checkAnswer(self, check):
        if(check == self.answer):
            return True
        else:
            return False