def html_special_chars(data): 
    symbols = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
    return "".join(symbols.get(x, x) for x in data)


def html_special_chars(data): 
    return data.translate(str.maketrans({'<':'&lt;','>':'&gt;','"':'&quot;','&':'&amp;'}))


def html_special_chars(data): 
    return data.replace('&', "&amp;").replace('>', "&gt;").replace('<', "&lt;").replace('\"', "&quot;")


def html_special_chars(data):    
    return data\
        .replace('&', '&amp;')\
        .replace('<', '&lt;')\
        .replace('>', '&gt;')\
        .replace('"', '&quot;'
                 
                 
from html import escape

def html_special_chars(data): 
    return escape(data).replace('&#x27;', '\'')