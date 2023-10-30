"""Feladat:
Az alábbi 2 függvény a debuggolást könnyíti azzal, hogy lefutás előtt kiír egy üzenetet.
Készíts egy @debug dekorátort, amely bármilyen függvényt képes hasonló üzenetkiírással kiegészíteni!
Kerüljön kiírásra a meghívott függvény neve és a kapott paraméterek értékei is!
"""


debug_mode = True

def debug(cb):
    def wrapper(*args, **kwargs):
        if debug_mode:
            # f"{a!r}" is equivalent to repr(a)
            args_repr = [f"{a!r}" for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            print(f"{cb.__name__} called with arguments:" + ", ".join(args_repr + kwargs_repr))
        return cb(*args, **kwargs)
    return wrapper

def greet(lang: str = "en") -> str:
    if debug_mode:
        print("greet called with arguments: " + lang) #?
    if lang == "en":
        return "Hello"
    elif lang == "de":
        return "Hallo"
    elif lang == "hu":
        return "Helló"
    else:
        return "Hello"

@debug
def my_print(*args, **kwargs):
    # if debug_mode:
    #     # f"{a!r}" is equivalent to repr(a)
    #     args_repr = [f"{a!r}" for a in args]
    #     kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    #     print("my_print called with arguments:" + ", ".join(args_repr + kwargs_repr))
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    print()
    print("=" * len(f"{sep.join(args) + end}".rstrip()))
    print(*args, **kwargs)
    print("=" * len(f"{sep.join(args) + end}".rstrip()))
    print()


# Segítség a függvény nevének lekérdezéséhez
def func_name(func) -> str:
    return func.__name__


my_print(greet("hu"), "világ", end="!\n")
my_print(greet("en"), "world", "with", func_name(my_print), end="!\n", sep=" ")
