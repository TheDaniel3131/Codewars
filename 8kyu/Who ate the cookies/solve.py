def cookie(x):
    if type(x) is str: 
        return "Who ate the last cookie? It was Zach!"
    elif type(x) is int or type(x) is float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
    
    
def cookie(x):
    if isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    elif isinstance(x, bool):
        return "Who ate the last cookie? It was the dog!"
    elif isinstance(x, (float, int)):
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
    
    
def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")


def cookie(x):
    return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'


def cookie(x):
    types = {
        'str': 'Zach',
        'int': 'Monica',
        'float': 'Monica'
    }
        
    return 'Who ate the last cookie? It was {0}!'.format(
            types.get(type(x).__name__, 'the dog'))
        
