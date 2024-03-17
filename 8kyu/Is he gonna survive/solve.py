def hero(bullets, dragons):
    if bullets == 0 or bullets < dragons:
        return False
    return (bullets // dragons) % 2 == 0


def hero(bullets, dragons):
    return bullets >= dragons * 2



def hero(bullets, dragons):    
    return (1 if bullets//dragons == 2 else 0)

def hero(bullets, dragons):
    return int(bullets) >= int(dragons * 2)