def fact(n):
    #"iterativley"#
    if n > 1:
        for f in range(2, n+1):
            result+=f
    return result

    
def factorial(n):
    # n can be defined as n+(n-1):
    """ caclulates n! recursiley """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """ F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)



print(factorial(2))