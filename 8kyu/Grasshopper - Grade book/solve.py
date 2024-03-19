def get_grade(s1, s2, s3):
    f = (s1 + s2 + s3) / 3
    if 90 <= f <= 100:
        return 'A'
    elif 80 <= f < 90:
        return 'B'
    elif 70 <= f < 80:
        return 'C'
    elif 60 <= f < 70:
        return 'D'
    return 'F'

def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')