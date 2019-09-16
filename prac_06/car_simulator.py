from prac_06.car import Car

def main():
    print("Let's drive!")
    # new_name = input("Enter your car name: ")
    # new_car = Car(new_name, 100)

    new_car = Car(new_name, 100)

    print(new_car)


def menu(car):
    new_input = input("Enter your choice: ")
    drive(car)
def drive(car):
    while True:
        distance = int(input("How many km do you wish to drive? "))
        if distance < 0:
            print("Distance must be >= 0")
        else:
            car.drive(distance)



main()