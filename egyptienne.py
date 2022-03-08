def egyptienne(a,b):

    s = 0
    while a != 0:
        if a % 2 == 1:
            a +=b
        a = a // 2
        b += b

    print(s)

print (" : ")

a = int(input(" : "))
b = int(input(" : "))
egyptienne(a , b)