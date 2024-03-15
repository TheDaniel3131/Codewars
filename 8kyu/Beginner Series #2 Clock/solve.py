def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        return ((h * 3600) + (m * 60) + s) * 1000
    else:
        return 0;