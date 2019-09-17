from prac_06.car import Car

def main():
    print("Let's drive!")
    new_name = input("Enter your car name: ")
    new_car = Car(new_name, 100)

    # new_car = Car("The Bomb", 100)

    # print(new_car)
    menu(new_car)

def menu(car):

    # new_input = input("Enter your choice: ")
    check = True
    while check:
        print("Menu:\nd) drive\nr) refuel\nq) quit")
        new_input = input("Enter your choice: ")
        if new_input.lower() == "d":
            drive(car)
        elif new_input.lower() == "r":
            refuel(car)
        elif new_input.lower() == "q":
            print("Good bye {}'s driver.".format(car.name))
            check = False
        else:
            print("Invalid choice")


def drive(car):
    check = True
    distance = int(input("How many km do you wish to drive? "))
    while check:
        if distance < 0:
            print("Distance must be >= 0")
        else:
            check = False
            odometer_before = car.odometer
            car.drive(distance)
            odometer_after = car.odometer
            if car.fuel > 0:
                print("The car drove {}km.".format(distance))
            else:
                print("The car drove {}km and ran out of fuel.".format(odometer_after - odometer_before))


def refuel(car):
    while True:
        new_fuel = int(input("How many units of fuel do you want to add to the car? "))
        if new_fuel < 0:
            print("Fuel amount must be >= 0")
        else:
            car.add_fuel(new_fuel)
            print("Added {} units of fuel.".format(new_fuel))
            return


main()