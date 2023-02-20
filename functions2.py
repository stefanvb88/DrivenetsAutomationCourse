#create our own functions

def our_function():
    """
    This is my first function, it just prins 'hello'
    :return: None
    """
#    print("hello")

    pass # this is an empty function

our_function()
help(our_function)

def our_function2(name):
    """
    This is my second function, it prints  hello {name}
    :param name: the name of the person to greet
    :return: None
    """
    print(f"Hello {name} !")

our_function2("Stefan")
help(our_function2)


def our_function3(a, b, c):
    """
    Adds a, b, c and print the result
    :param a: first value
    :param b: second value
    :param c: thrid value
    :return: None
    """
    result = a + b + c
    print(f"The result of adding {a}, {b}, {c} is {result} .")
our_function3(1,2,3)



def our_function4(a, b, c):
    """
    Adds a, b, c and print the result
    :param a: first value
    :param b: second value
    :param c: thrid value
    :return: None
    """
    result = a + b + c
    return result
 #   print(f"The result of adding {a}, {b}, {c} is {result} .")
print(our_function4(1,2,3))
#print(f"I can use this {result}")


def our_function5(a: int =10, b: int =20, c: int =30):
    """
    Adds a, b, c and print the result
    :param a: first value
    :param b: second value
    :param c: thrid value
    :return: None
    """
    result = a + b + c
    return result


print(our_function5())
print(our_function5(c=100))
