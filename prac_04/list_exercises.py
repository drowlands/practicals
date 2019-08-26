def main():
    numbers = []
    total = 0
    average = 0

    print("Please provide five numbers.")
    for count in range(5):
        numbers.append(int(input("Number: ")))
    print("The first number is %d" % (numbers[0]))
    print("The last number is %d" % (numbers[-1]))
    print("The smallest number is %d" % (min(numbers)))
    print("The largest number is %d" % (max(numbers)))

    for number in numbers:
        total += number
    average = total / len(numbers)

    print("The average of the number is %d" % (average))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_login = input("Please provide a username: ")
    if (user_login in usernames):
        print("Access granted")
    else:
        print("Access denied")

main()
