class Player:
    def __init__(self, name):
        self.name = name
        
def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name 
    
    
def duck_duck_goose(players, goose):
    return players[(goose % len(players)) - 1].name


def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name