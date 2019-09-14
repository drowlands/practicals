from prac_06.guitar import Guitar

def main():
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Another Guitar", 2012, 12345.67)

    print("{} get_age() - Expected {}. Got {}".format(first_guitar.name, first_guitar.year, first_guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(second_guitar.name, second_guitar.year, second_guitar.get_age()))

    print("{} is_vintage() - Expected {vintage}. Got {}".format(first_guitar.name, vintage=True if (2019 - first_guitar.year) > 50 else False, first_guitar.is_vintage()))
    print("{} is_vintage() - Expected {vintage}. Got {}".format(second_guitar.name, vintage=True if (2019 - second_guitar.year) > 50 else False, second_guitar.is_vintage()))

    first_guitar.get_age()
    first_guitar.is_vintage()