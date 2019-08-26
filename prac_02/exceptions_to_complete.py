"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter an integer: "))
        if type(result) == int:
            finished = True
        pass
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
    # finished = True
print("Valid result is:", result)
