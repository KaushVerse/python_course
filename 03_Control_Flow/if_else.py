# Basic if Statement
age = 20
if age >= 18:
    print('You are eligible to vote.')


# if else statement
age = 15
if age >= 18:
    print('You can vote')
else: 
    print('You cannot vote.')


# if elif else
marks = 75
if marks >= 90:
    print('Grade A+')
elif marks >= 75:
    print('Grade A')
elif marks >= 50:
    print('Grade B')
else:
    print('Fail')

    
# Nested if (if ke andar if)
age = 25
has_id = True

if age >= 18:
    if has_id:
        print('Entry allowed.')
    else: 
        print('ID required')
else:
    print('Age restriction.')


# Short-Hand if (One-Liner if)
x = 10
if x > 5: print('Greater than 5')


# Short-Hand if else (Ternary Operator)
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)


# Conditional Expressionns in Assignment
marks = 80
grade = (" A+" if marks >= 90
        else " A" if marks  >= 75
        else " B")

print(grade)


# Using and | or in if Conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print('You can drive.')


# Using Membership Operators with if
fruits = ['apple', 'mango', 'banana']

if "mango" in fruits:
    print('Mango is available.')