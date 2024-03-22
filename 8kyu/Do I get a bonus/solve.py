def bonus_time(salary, bonus):
    return f"${salary * 10}" if bonus == 1 else f"${salary}"

def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1)
                        

                        
# this solution is crazy.. it uses array indexing method.
                        
# How do you know whether it will pick 1 or 10? Does the first element always correspond with False and the second with True?

# If bonus is False, its index value is 0 consider: array = ['a', 'b'] bonus = True array[bonus] == array[1] == 'b' bonus = False array[bonus] == array[0] == 'a'
                        
                        
def bonus_time(salary, bonus):
    return '$' + str(salary * [1,10][bonus])
                        