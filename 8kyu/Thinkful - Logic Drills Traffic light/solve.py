def update_light(current):
    if current == "red":
        return "green"
    elif current == "yellow":
        return "red"
    else:
        return "yellow"
    
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


def update_light(current):
    light_order = {'red':'green', 'yellow':'red', 'green':'yellow'}
    
    return light_order[current]

def update_light(current):
    match current:
        case 'red': return 'green'
        case 'yellow': return 'red'
        case 'green': return 'yellow'
        
update_light = {"green":"yellow", "yellow":"red", "red":"green"}.get