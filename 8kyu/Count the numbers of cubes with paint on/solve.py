def count_squares(cuts):
    if cuts == 0:
        return 1; #only one square
    else:
        return ((cuts+1) ** 3) - ((cuts-1) ** 3)