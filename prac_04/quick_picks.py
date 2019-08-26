import random

MAXIMUM_VALUE = 1
MINIMUM_VALUE = 45

def main():

    pick_count = int(input("How many picks do you want? "))
    for pick in range(pick_count):
        # Generate line
        # line = ""
        numbers_in_line = []
        while len(numbers_in_line) < 6:
            new_number = random.randint(1, 45)
            if new_number not in numbers_in_line:
                # print("Hit")
                numbers_in_line.append(str(new_number) + "\t")
        line = "".join(numbers_in_line)
        print(line)

main()