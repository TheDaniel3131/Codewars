def cube_checker(volume, side):
    if volume < 1 and side < 1:
        return False;
    elif (side ** 3) == volume:
        return True;
    else:
        return False;