"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When one of the values entered is not a number.
2. When will a ZeroDivisionError occur?
When one or both of the values entered is a zero.
3. Could you change the code to avoid the possibility of a zeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while numerator == 0 or denominator == 0:
        if numerator == 0:
            numerator = int(input("Enter a valid numerator: "))
        else:
            denominator = int(input("Enter a valid denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
