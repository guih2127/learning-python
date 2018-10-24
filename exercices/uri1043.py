a, b, c = (input().split(" "))
a, b, c = float(a), float(b), float(c)

if (a < b + c) and (a > abs(b - c)):
    if (b < a + c) and (b > abs(a - c)):
        if (c < a + b) and (c > abs(a - b)):
            x = (a + b + c)
            print('Perimetro = ' + str(x))
else:
    x = ((a + b) / 2) * c
    print('Area = ' + str(x))
        
            