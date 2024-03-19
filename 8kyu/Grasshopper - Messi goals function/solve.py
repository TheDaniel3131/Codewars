def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


def goals(*args):
    return sum(args)