from prac_06.guitar import Guitar

def main():
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Another Guitar", 2012, 12345.67)

    print("{} get_age() - Expected {}. Got {}".format(first_guitar.name, 2019 - first_guitar.year, first_guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(second_guitar.name, 2019 - second_guitar.year, second_guitar.get_age()))

    if (2019 - first_guitar.year) > 50:
        vintage_first = True
    else:
        vintage_first = False

    if (2019 - second_guitar.year) > 50:
        vintage_second = True
    else:
        vintage_second = False


    print("{} is_vintage() - Expected {vintage}. Got {check}".format(first_guitar.name, vintage=vintage_first, check=first_guitar.is_vintage()))
    print("{} is_vintage() - Expected {vintage}. Got {check}".format(second_guitar.name, vintage=vintage_second, check=second_guitar.is_vintage()))

    first_guitar.get_age()
    first_guitar.is_vintage()

main()