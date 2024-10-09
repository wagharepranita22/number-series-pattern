# check if a number is km , special number or not . where sum of factorial of digits is equal to
#the number e.g 145 = 1!+4!+5!
import math
n = int(input("Give n Number  : "))
copy = n
sum = 0

while n != 0:
    d = n % 10
    sum += math .factorial(d)
    n = n // 10

if sum == copy:
    print("number is special number")
else:
    print("number is not special number")