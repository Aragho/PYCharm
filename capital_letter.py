def check_capital_letter(user):
    user1 = ""
    user2 = ""
    for letter in user:
        if letter.isupper():
            user1 += letter
        else:
            user2 += letter
    return user1 + user2