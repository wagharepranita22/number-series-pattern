# check if a number is neon number or not. where sum of digit of square of the number is equal to the number of the number  eg 9,9*9 =81 ,9 =8+1
n = int(input("Give n Number  : "))
copy = n
sum = 0
squar = n*n
while squar != 0:
    d = squar % 10
    sum += d
    squar = squar // 10

if sum == copy:
    print("number is neon number")
else:
    print("number is not neon number")