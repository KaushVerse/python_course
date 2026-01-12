# Input

# input() ek function hai jp user se data leta hai 
# By default string return karta hai.
# Type conversion manually karna padta hai(int(), float())

name = input('Enter your name: ')

# print() ek function hai jo data ko console main dikhate hai
# Multiple values, formatting, end  & sep options support karta hai.

print('Hello', name)

# Example with type conversion
age = int(input('Enter your age: '))
print(f"You are {age} years old.")