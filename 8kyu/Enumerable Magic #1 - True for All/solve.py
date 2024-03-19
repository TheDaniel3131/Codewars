def _all(seq, fun): 
    return all(map(fun,seq))
   
   
def _all(seq, fun):
    return all(fun(i) for i in seq)
    
def all(seq, fun):
    return next((False for x in seq if not fun(x)), True)
    
from builtins import all as shrug

def all(seq, fun): 
    return shrug(map(fun, seq))