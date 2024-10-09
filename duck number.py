# check if a number id duck number or not a number which has zeroes present in it eg 402 280
n = int(input("Give n Number  : "))
count = 0
while n != 0:
    d = n % 10
    if d == 0:
        count +=1
    n = n // 10


if count >= 1 :
    print("number is duck number")
else:
    print("number is not duck number")