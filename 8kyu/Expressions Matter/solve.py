def expression_matter(a, b, c):
    # output possible expressions with maximum value
    return max(a * (b + c), a * b * c, (a + b) * c, a + b + c)


def expression_matter(a, b, c):
    operations = '+*'
    return max(
        max(eval(f'({a}{op1}{b}){op2}{c}'), eval(f'{a}{op1}({b}{op2}{c})'))
        for op1 in operations
        for op2 in operations
    )