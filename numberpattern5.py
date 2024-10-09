# /Pyramid Number Pattern
n = int(input("n : "))
for i in range(n,0,-1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n,1):
        print(i,end=" ")
    for j in range(i,n,1):
        print(i, end=" ")

    print()



for i in range(1,n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i+1,n):
        print(i,end=" ")
    for j in range(i,n):
        print(i, end=" ")

    print()
