def count_letter(character):
    my_dict = {}
    for letter  in character:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    return my_dict
print(count_letter("semicolon.africa"))


