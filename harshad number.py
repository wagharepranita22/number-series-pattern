# check if a number is harshad/niven number or not. a  umber which is divisible by the sum of its digit .e.g 156  =1+5+6 =12

n = int(input("Give n Number  : "))
copy = n
sum = 0
prod = 1
while n != 0:
    d = n % 10
    sum += d
    n = n // 10


if copy % sum == 0:
    print("number is harshad/niven number")
else:
    print("number is not s harshad/niven number")