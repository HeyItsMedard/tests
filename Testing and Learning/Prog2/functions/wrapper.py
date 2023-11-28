def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25) 
"""display_info is given as an argument to decorator_function due to decorator
decorator_function runs the wrapper_function inside
the print runs first and then returns with the orignal function
display_info finally prints"""

display()
