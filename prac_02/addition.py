number_file = open("numbers.txt", "r")
value = 0
for line in number_file:
    value += int(line)
print("Value is", value)
number_file.close()