x = lambda n: n+n
print(x(2), x(3), x(5))

print((lambda n: n+n)(10))

def increase(n):
    """
    Use to construct different increase functions
    :param n: The number of times to increase
    :return: a lambda function
    """
    return lambda x : x*n

double = increase(2)
triple = increase(3)
tenfold = increase(10)

print(double(10), triple(20), tenfold(100))

power = lambda x, y: x**y
print(power(2,3))
#the same with def
#def power(x, y):
#    result = x**y
#    print(result)
#power(2,3)

#map
print(list(map(lambda x: x.upper(), "abcdefghjiklm")))

#filter
print(list(filter(lambda x : x < 5, list(range(-100,100)))))
