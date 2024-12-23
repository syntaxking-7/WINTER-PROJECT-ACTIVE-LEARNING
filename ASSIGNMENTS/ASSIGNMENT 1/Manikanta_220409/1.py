def fibonacci(n):
    a = 1;
    b = 1;
    for i in range(n):
        print(i, " --> ",a)
        c = b
        b += a
        a = c

fibonacci(10)


    
