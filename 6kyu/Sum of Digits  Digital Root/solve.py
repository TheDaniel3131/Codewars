def digital_root(n): 
    return n if n < 10 else digital_root(sum(int(i) for i in str(n)))


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


def digital_root(n):
	return n % 9 or n and 9 


