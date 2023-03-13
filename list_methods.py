print(dir([]))

list(filter(lambda x: not x.startswith("__"), dir([])))