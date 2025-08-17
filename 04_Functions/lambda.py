# Normal Function
def add(a, b):
    return a + b

print(add(5, 3))


# Lambda Function
add = lambda a, b: a + b

print(add(5, 3))


# Another Example
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))

print(squares)