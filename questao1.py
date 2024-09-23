def fib(n):
    a, b = 0, 1
    num_fib = []
    #print(a, b)
    for i in range (n):
        num_fib.append(a)
        #print(num_fib)
        sum_fib = a + b
        a, b = b, a + b

    if n in num_fib:
        print(f"{n} pertence a sequencia")
    else:
        print(f"{n} nao pertence a sequencia")

n = 8
fib(n)