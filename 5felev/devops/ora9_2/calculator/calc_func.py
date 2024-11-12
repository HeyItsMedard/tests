def add(a, b):
    """Adds two numbers
    >>> add(1, 2)
    3
    
    :param a: first number
    :param b: second number
    :return: sum of a and b
    """
    return a+b

def subtract(a, b):
    """Subtracts two numbers
    >>> subtract(1, 2)
    -1
    >>> subtract(2, 1)
    1
    
    :param a: first number
    :param b: second number
    :return: difference of a and b
    """
    return a-b

def multiply(a, b):
    """Multiplies two numbers
    >>> multiply(1, 2)
    2
    >>> multiply(5, 2)
    10
    
    :param a: first number
    :param b: second number
    :return: product of a and b
    """
    return a*b

def divide(a, b):
    """Divides two numbers
    >>> divide(1, 2)
    0.5
    
    >>> divide(1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero
    
    :param a: first number
    :param b: second number
    :return: quotient of a and b
    """
    return a*1.0/b

def minimum(a, b):
    """Returns the lesser of two numbers
    >>> minimum(1, 2)
    1
    >>> minimum(2, 1)
    1
    >>> minimum(1, 1)
    1
    
    :param a: first number
    :param b: second number
    :return: lesser of a and b
    """
    return a if a<=b else b

def maximum(a, b):
    """Returns the greater of two numbers
    >>> maximum(1, 2)
    2
    >>> maximum(2, 1)
    2
    >>> maximum(5, 5)
    5
    
    :param a: first number
    :param b: second number
    :return: greater of a and b
    """
    return a if a>=b else b

if __name__ == '__main__':
    import doctest
    import xmlrunner

    suite = doctest.DocTestSuite()
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    runner.run(suite)
