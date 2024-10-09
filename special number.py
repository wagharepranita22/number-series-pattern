# check if a number is special number or not sum of digits plus producyt of digits it is equal to original number eg 59 = 5+9+5*9

n = int(input("Give n Number  : "))
copy = n
sum = 0
prod = 1
while n != 0:
    d = n % 10
    sum += d
    prod *= d
    n = n // 10

special = sum +prod

if special == copy:
    print("number is special number")
else:
    print("number is not special number")