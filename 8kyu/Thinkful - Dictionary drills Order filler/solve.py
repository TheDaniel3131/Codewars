def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False

def fillable(stock, merch, n):
    return merch in stock and stock[merch] >= n


def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n


def fillable(stock, merch, n):
    return stock.get(merch, False) >= n  