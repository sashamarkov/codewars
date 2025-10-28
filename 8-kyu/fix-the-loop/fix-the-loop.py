def list_animals(animals):
    result = ''
    i = 1
    for animal in animals:
        result += '{0}. {1}\n'.format(i, animal)
        i += 1
    return result