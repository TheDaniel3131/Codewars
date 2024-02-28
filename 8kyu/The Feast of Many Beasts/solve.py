def feast(beast, dish):
    beast = beast.strip("-").replace(" ","")
    dish = dish.strip("-").replace(" ","")

    return beast[0] == dish[0] and beast[-1] == dish[-1]