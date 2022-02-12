def star(row):
    for i in range(row+1,0,-1):
        for j in range(i):
            print("*",end='')
        print()
star(10)        