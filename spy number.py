# check the spy number means sum of its digits equals the product of the digits eg
# 123 .1 +2+3 = 1*2*3
n = int(input("Give n Number  : "))
copy = n
sum = 0
prod = 1
while n != 0:
    d = n % 10
    sum += d
    prod *= d
    n = n // 10

if sum == prod:
    print("number is spy number")
else:
    print("number is not spy number")