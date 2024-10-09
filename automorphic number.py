# check if a number is automorphioc number or not it is a number which is contained in the the last digits(s) of its square eg 25 = 625
n = int(input("Give n Number  : "))
copy = n
sum = 0
flag = 0
squar = n*n
while n != 0:
    d =n %10
    d1 = squar % 10
    if d != d1:
        flag +=1
    n = n//10
    squar = squar // 10

if flag == 0:
    print("number is automorphic number")
else:
    print("number is not automorphic number")