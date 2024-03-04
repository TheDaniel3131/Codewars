def divisible_by(numbers, divisor):
    output = []
    for number in numbers:
        if number % divisor == 0:
            output.append(number)
    return output