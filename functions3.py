# here we call functions from functions

def introduce(name):
    """

    :param name: a regular string
    :return: prints the name
    """
    print(f"The name is {name}")

def bond(first_name: str = "james", last_name: str = "bond") -> object:
    """
    Coll function
    :param first_name: first name, default "james"
    :param last_name: last name, default "bond"
    :return: returns the cool introduction
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{last_name}, {first_name} {last_name}"
introduce(bond())
introduce(bond("Stefan", "vlad"))
introduce(bond(first_name="John" ))
help(bond)