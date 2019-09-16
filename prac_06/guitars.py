from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # prompt(guitars)

    index = 1
    for guitar in guitars:
        print("Guitar {i}: {guitar.name} ({guitar.year}), worth $ {guitar.cost} {vintage_status}".format(i=index, guitar=guitar, vintage_status="(vintage)" if guitar.is_vintage() else ""))
        index += 1


def prompt(guitars):
    user_input=""

    while True:
        new_name = input("Name: ")

        if new_name == "":
            return False

        new_year = int(input("Year: "))
        new_cost = float(input("Cost: $"))
        guitars.append(Guitar(new_name, new_year, new_cost))



main()