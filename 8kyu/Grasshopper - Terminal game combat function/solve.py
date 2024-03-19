def combat(health, damage):
    return health - damage if health > damage else 0
    
def combat(health, damage):
    return max(0, health - damage)
    