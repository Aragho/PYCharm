def capital(character):
        character = character.replace("-","_")
        words = character.split("_")
        return words[0] + ''.join(word.capitalize() for word in words[1:])
