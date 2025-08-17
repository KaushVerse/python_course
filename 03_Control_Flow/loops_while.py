# while loop (Condition Based Loop)

count = 1
while count <= 5:
    print(count)
    count += 1


# while Loop with else
x = 1
while x <= 3:
    print(x)
    x += 1
else:
    print('Done')


# Infinite Loop (Manual Break)
# while True:
#     name = input("Enter name (or 'q' to quit):")
#     if name == 'q':
#         break


# break Statement (Exit Loop)
for i in range(5):
    if i == 3:
        break
    print(i)


# continue Statement (Skip Iteration)
for i in range(5):
    if i == 2:
        continue
    print(i)


# List Comprehension Loop
squares = [x*x for x in range(5)]
print(squares)


# Loop with enumerate() (index + value)
fruits = [ 
    "🍎",  # Red Apple
    "🍏",  # Green Apple
    "🍐",  # Pear
    "🍊",  # Tangerine
    ]

for index, fruit in enumerate(fruits):
    print(index, type(fruit))