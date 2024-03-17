def hero(bullets, dragons):
    if bullets == 0 or bullets < dragons:
        return False
    return (bullets // dragons) % 2 == 0