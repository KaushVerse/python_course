# Operator           Symbol          Description                      Example    Ouutput
# +Add                 +       Do numbers ko jodta hai                 5 + 3       8
# -Subtract            -       Ek number ko dusre se ghata hai         5 - 3       2
# *Multiply            *       Dono numbers ko multiply karta hai      5 * 3       15
# /Divide              /       Normal division (float result)          5 / 3       2.5
# // Floor Dive        //       Division but integer result            5 // 2       2
# %Modulo              %       Remainder deta hai                      5 % 3       1
# **Exponent           **      Power ka exponential karta hai          2 ** 3      8


a = int(input('Enter a: '))
b = int(input("Enter b: "))

print(f"+ {a + b}")
print(f"- {a - b}")
print(f"* {a * b}")
print(f"/ {a / b}")
print(f"// {a // b}")
print(f"% {a % b}")
print(f"** {a ** b}")