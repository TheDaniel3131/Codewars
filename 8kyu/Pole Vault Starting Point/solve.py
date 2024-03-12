def starting_mark(height):
    # vaulter's height 1.52 meters -> 9.45 meters runaway
    # vaulter's height 1.83 meters -> 10.67 meters runaway
    # vaulter's height range: min 1.22 meters to max 2.13 meters
    
    if height < 1.22 or height > 2.13:
        return None

    # y= mx + c, m is slope, x is height, c is y-intercept
    
    # find slope
    m = (10.67 - 9.45) / (1.83 - 1.52) # can pick any mark as long it is ranged

    # find y-intercept
    c = 9.45 - (m * 1.52)

    # find the best starting mark
    mark =(m * height) + c
    return round(mark, 2)