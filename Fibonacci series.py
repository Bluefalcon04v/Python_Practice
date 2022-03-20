'''give fibonacci series''' 

x = int(input("up-to what number you want fibonacci series to be printed \n"))

def fib():
    a = 0
    b, c = 1, 1
    z = globals()['x']
    if z == 1:
        print(a)
    else:
        print(a)
        print(b)
        while c < z and a + b <= z:
            c = a + b
            a = b
            b = c
            print(c)
            c += 1

fib()
