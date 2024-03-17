def find_average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)


def find_average(array):
    return sum(array) / len(array) if array else 0