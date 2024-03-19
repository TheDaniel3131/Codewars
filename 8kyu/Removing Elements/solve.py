def remove_every_other(my_list):
    return [y for x, y in enumerate(my_list) if x % 2 == 0]
    
    
    
 def remove_every_other(my_list):
    return my_list[::2]