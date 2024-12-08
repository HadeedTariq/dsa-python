def patter_printer(n):
    i = 0
    while n > i:
        pattern = ""
        for k in range(n):
            pattern = pattern + " *"
        print(pattern)
        n = n - 1


patter_printer(5)
