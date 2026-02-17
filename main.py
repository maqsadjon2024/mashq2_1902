#72
def gen_juft(n):
    for i in range(2, n+1, 2):
        yield i

print(list(gen_juft(10)))

#73
def gen_fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

print(list(gen_fib(7)))

#74
def binary(n):
    return bin(n)[2:]

print(binary(10))

#75
def decimal(b):
    return int(b, 2)

print(decimal("1010"))

#76
def flatten(lst):
    natija = []
    for x in lst:
        if isinstance(x, list):
            natija.extend(flatten(x))
        else:
            natija.append(x)
    return natija

print(flatten([1,[2,3],[4,[5,6]]]))
