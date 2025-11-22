# Normal Loop
squares = []
for x in range(6):
    squares.append(x * x)

print(squares)


# List Comprehensions

squares = [x * x for x in range(6)]
print(squares)


# With Condition

evens = [x for x in range(10) if x % 2 == 0]
print(evens)


# With if-Else
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(6)]
print(labels)


# Set Comprehensions
nums = {x * x for x in [1, 2, 2, 3, 4]}
print(nums)


# Dictionary Comprehensions
evens = {x: x * x for x in range(10) if x % 2 == 0}
print(evens)


# Generator Expression 
gen = (x * x for x in range(6))
print(next(gen))
print(next(gen))
print(next(gen))