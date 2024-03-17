def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi <= 25:
        return "Normal"
    elif 25 < bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"
        
def bmi(weight, height):
    bmi = weight / height ** 2
    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"

def bmi(weight, height):
    b = weight / height ** 2
    # using index method
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]


# explanation on third solution
# you can add boolean values in Python (True -> 1, False -> 0). For example, if b == 27 then you get for (b > 30) + (b > 25) + (b > 18.5) -> False + True + True -> 0 + 1 + 1 -> 2 ['Underweight', 'Normal', 'Overweight', 'Obese'][2] -> 'Overweight'