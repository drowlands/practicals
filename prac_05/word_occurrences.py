def main():
    # Declare variables
    biggest_word = 0
    new_word_list = {}
    text_string = input('Please enter a string: ')
    string_list = text_string.split()

    # Loop through items in string list. If item has not been seen before, set value to one, otherwise increase by one.
    for word in string_list:
        if word not in new_word_list:
            new_word_list[word] = 1
        else:
            new_word_list[word] += 1

    # Find biggest word length
    for word in new_word_list:
        if len(word) > biggest_word:
            biggest_word = len(word)
    print('Text: {}'.format(text_string))

    # Sort pairs and print values with padding
    for pair in sorted(new_word_list.keys()):
        print("{:{}} = {}".format(pair, biggest_word + 1, new_word_list[pair]))
main()