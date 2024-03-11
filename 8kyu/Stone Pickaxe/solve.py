def stone_pick(arr):
    ## Question says that we need to find out the maximum possible pickaxes
    # One single stone pickaxe = 3 cobblestone & 2 sticks
    
    # First we can set some variables here
    count_cobblestone = arr.count("Cobblestone")
    count_sticks = arr.count("Sticks")
    count_wood = arr.count("Wood")
    
    # Wood can be converted into 4 sticks
    # In this case, we need to multiply the woods 4 times to get a stick
    # The reason I have to add "count_sticks" again is because "count_sticks" will be replaced with new value..
    # If I do like this "count_sticks = count_wood * 4"
    count_sticks = count_sticks + (count_wood * 4)
    
    # Use minimum function for minimum materials to craft a pickaxe
    pickaxe = min(count_cobblestone // 3, count_sticks // 2)

    # If else statements
    # Empty array & no picks
    if arr is None and arr == 0:
        return 0;
    else: 
        return pickaxe;
        