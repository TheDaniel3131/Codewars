def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)
        self.gender = "male"

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)
        self.gender = "female"
