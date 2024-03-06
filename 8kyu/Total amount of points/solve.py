# my solution
def points(games):
    result = 0
    for match in games:
        x, y = map(int, match.split(":"))
        if x > y:
            result += 3
        elif x < y:
            result += 0
        else:
            result += 1
    return result


# others
def points(games):
    return sum(3 if x > y else 0 if x < y else 1 for x, y in (score.split(":") for score in games))


def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count