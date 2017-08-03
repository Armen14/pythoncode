def f0():
    c = 1
    b = 1
    a = 1
    sum = 0
    i = 3
    f = "Vvedite N"
    n = input(f)
    f5(n,a, b, c, sum, i)
def f5(n,a, b, c, sum, i):
    if n < 0:
        print "n < 0"
    else:
        f6(n, a, b, c, sum, i)
def f6(n, a, b, c, sum, i):
    if n == 1:
        print "summa ne izmenitsya"
    else:
        f7(n,a, b, c, sum, i)
def f7(n,a, b, c, sum, i):
    if n == 2:
        print "Summa ne izmenitsya"
    else:
        f9(n,a, b, c, sum, i)
def f9(n,a, b, c, sum, i):
    if i <= n:
        c = a + b
        b = a
        a = c
        sum+=c
        f9(n, a, b, c,sum, i = i+1)
    else:
        fsum(n,a, b, c, sum, i)
def fsum(n,a, b, c, sum, i):
    print sum
print f0()