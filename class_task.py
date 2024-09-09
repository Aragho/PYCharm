def count_in_dict(word):
    my_dict = {}
    for letter in word:
        my_dict[letter.lower()] = my_dict.get(letter.lower(), 0) + 1
    return my_dict

