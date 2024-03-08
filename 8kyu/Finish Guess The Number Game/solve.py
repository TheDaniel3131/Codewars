class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
    
    def guess(self, n):
        self.n = n
        if self.lives < 1:
            raise ValueError("Omae wa mo shindeiru")
        elif self.number == self.n:
            return True
        else:
            self.lives -= 1
            return False