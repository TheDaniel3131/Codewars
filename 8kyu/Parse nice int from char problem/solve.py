def get_age(x):
    return int(x[0])
    
    
def get_age(age):
    for x in age:
    	if x.isdigit():
        	return int(x) 
 
import re

def get_age(age):
    return int(re.search(r"\d+", age).group())
    
    
def get_age(age):
    return int(age[:1])