def switch_it_up(number):
    match number:
        case 0:
            return "Zero"
        case 1: 
            return "One"
        case 2:
            return "Two"
        case 3: 
            return "Three"
        case 4:
            return "Four"
        case 5: 
            return "Five"
        case 6:
            return "Six"
        case 7:
            return "Seven"
        case 8:
            return "Eight"
        case 9:
            return "Nine"
        case _:
            return "It is not between 0-9!"
            
def switch_it_up(number):
    dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"}
    
    return dict.get(number)




def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]