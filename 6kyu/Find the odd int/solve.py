def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            print(i)
            return i
            
        