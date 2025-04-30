output=0
for x in range(1,10):
    for y in range(1,10):
        output=x*y
        print("%d x %d = %d" %(x,y,output),end="    ")
    print("\n")