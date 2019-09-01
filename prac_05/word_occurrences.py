def main():
    biggest_word = 0
    new_word_list = {}
    text_string = input('Please enter a string: ')
    string_list = text_string.split()
    for word in string_list:
        if word not in new_word_list:
            new_word_list[word] = 1
        else:
            new_word_list[word] += 1

    for word in new_word_list:
        if len(word) > biggest_word:
            biggest_word = len(word)
    print('Text: {}'.format(text_string))
    for pair in sorted(new_word_list.keys()):
        print("{:{}} = {}".format(pair, biggest_word + 2, new_word_list[pair]))
main()