def solution(string,markers):
    s_list = string.split('\n')
    for marker in markers:
        s_list = [item.split(marker)[0].rstrip() for item in s_list]
    return '\n'.join(s_list)
    
    
import re

def strip_comments(text, markers):
    return re.sub('|'.join('( |\t)*\\' + m + '[^\n]*' for m in markers), '', text)