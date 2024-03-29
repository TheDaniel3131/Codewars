def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif 14 <= age < 18:
        return "drink coke"
    elif 18 <= age < 21:
        return "drink beer"
    else:
        return "drink whisky"

    
def people_with_age_drink(age):
    match age:
        case age if age < 14:
            return 'drink toddy'
        case age if 14 <= age < 18:
            return 'drink coke'
        case age if 18 <= age < 21:
            return 'drink beer'
        case _:
            return 'drink whisky'
        
        
def people_with_age_drink(age):
    return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')


def people_with_age_drink(age):
    return ["drink toddy", "drink coke", "drink beer", "drink whisky"][(age >= 21) + (age > 17) + (age > 13)]



def people_with_age_drink(age):
    drinks = {age<14:'toddy',14<=age<18:'coke',18<=age<21:'beer',age>=21:'whisky'}
    return 'drink {}'.format(drinks[True])