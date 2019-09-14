COLOUR_LIST = {'aliceblue': '#f0f8ff', 'antiquewhite': '#faebd7', 'antiquewhite1': '#ffefdb',
               'antiquewhite2': '#ffefdb', 'antiquewhite3': '#cdc0b0', 'antiquewhite4': '#8b8378',
               'aquamarine1': '#7fffd4', 'aquamarine2': '#76eec6', 'aquamarine4': '#458b74', 'azure1': '#f0ffff'}


def main():
    colour = input('Please enter a colour name: ').lower()
    while colour != '':
        try:
            print(COLOUR_LIST[colour])
        except:
            print('Colour incorrect.')
        colour = input('Please enter a colour name: ').lower()

main()
