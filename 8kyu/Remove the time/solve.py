def shorten_to_date(long_date):
    for date in long_date.split(','):
        return date
        
        
def shorten_to_date(long_date):
    return long_date.split(',')[0]


def shorten_to_date(long_date):
    return long_date[:long_date.index(',')]


def shorten_to_date(long_date):
    return long_date[:long_date.rfind(',')]


def shorten_to_date(long_date):
    date, time = long_date.split(",")
    return date
            