from tokenize import tokenize

F0 = open(__file__, "rb")


def readline():
    return next(F0)


for tk in tokenize(readline):
    print(tk)
