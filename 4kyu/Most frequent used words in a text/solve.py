from re import findall
from collections import Counter

def top_3_words(text):
    splitted_word =  findall(r"[a-z']+", text.lower())  
    splitted_word = [word for word in splitted_word if word != "'" and any(char.isalpha() for char in word)]
    splitted_word_count = Counter(splitted_word)
    top_three_words = splitted_word_count.most_common(3)
    print(top_three_words)


    return [word for word, count in top_three_words]


