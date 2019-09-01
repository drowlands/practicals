def main():
    new_word_list = {}
    text_string = input('Please enter a string: ')
    string_list = text_string.split()
    for word in string_list:
        if word not in new_word_list:
            new_word_list[word] = 1
        else:
            new_word_list[word] += 1
    print('Text: {}'.format(text_string))
    for pair in sorted(new_word_list.keys()):
        print("{:{}} = {}".format(pair, 10, new_word_list[pair]))
main()