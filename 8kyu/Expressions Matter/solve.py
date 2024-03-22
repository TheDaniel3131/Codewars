def expression_matter(a, b, c):
    # output possible expressions with maximum value
    return max(a * (b + c), a * b * c, (a + b) * c, a + b + c)
