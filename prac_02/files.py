name_file = open("name.txt", "w")
name = str(input("What is your name? "))
print(name, file = name_file)
name_file.close()

name_file = open("name.txt", "r")
for name in name_file:
    print("Your name is", name)
name_file.close()

number_file = open("numbers.txt", "r")
value = 0
for line in number_file:
    value += int(line)
print("Value is", value)
number_file.close()

another_value = 0
file_name = str(input("What is the name of the file with the numbers? "))
many_numbers_file = open(file_name, "r")
for line in many_numbers_file:
    another_value += int(line)
print("Value is", another_value)
many_numbers_file.close()