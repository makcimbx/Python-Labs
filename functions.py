вывод = print

def add(x, y):
    return x + y

вывод(add(1, 10))
вывод(add('abc', 'def'))

def newfunc(n):
    def myfunc(x):
        return n + x
    return myfunc

вывод(newfunc(1)(2))