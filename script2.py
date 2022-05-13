print ("Second py script file")


def simple_square(side):
    '''
    this function prints the square of the input integer

    this particular line of docstring is intentionally here because it is not in the best practices of PEP8 and will hopefully be caught by a linter
    '''
    square = side**2
    print(square)
    return square


square = simple_square(4)
