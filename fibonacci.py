#0,1,1,2,3,5,8,13

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b, a+b

f=fib()


print(next(f))
