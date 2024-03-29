def rental_car_cost(day):
    total_amount = 40 * day
    if day >= 7:
        total_amount -= 50
    elif day >= 3:
        total_amount -= 20
    return total_amount


def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result



def rental_car_cost(d):
    return d * 40 - (d > 2) * 20 - (d > 6) * 30

