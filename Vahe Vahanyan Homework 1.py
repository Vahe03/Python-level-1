# 1
def my_decorator(func):
    def wrapper(n):
        result = n * 10
        return result

    return wrapper


@my_decorator
def number(n):
    return n


print(number(10))


# 2
def type_check(func):
    def wrapper(x, y):
        if isinstance(x, int) and isinstance(y, int):
            result = x + y
            return result
        else:
            raise TypeError

    return wrapper


@type_check
def add_integers(x, y):
    return x, y


print(add_integers(6, 2))


# 3
def listSum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + listSum(lst[1:])


print(listSum([1, 3, 4]))


# 4
def geo_sum(n, r=2, a=1):
    if n==1:
        return a*(r**1)
    else:
        result = (a * (r ** n)) + geo_sum(n-1)
        return result

print(geo_sum(3))
