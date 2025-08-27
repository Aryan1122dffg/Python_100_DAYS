def is_even(number):
    """TELLS if number is odd or even"""
    if type(number) == int:
        if number%2 == 0: 
            return("even")
        else:
            return("odd")
    else: 
        print("NOT allowed")


    