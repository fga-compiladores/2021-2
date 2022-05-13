import builtins

_str = str


def str_evil(x):
    if x == 666:
        return "numero do b17"
    elif x == 42:
        return "a resposta"
    else:
        return _str(x)


def dbg(x):
    print(f"dbg: {x}")
    return x


builtins.str = str_evil
builtins.dbg = dbg
