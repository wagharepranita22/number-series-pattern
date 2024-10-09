# print all digits of a number on different lines
n = int(input("Give n Number  : "))
copy  = n
while n != 0 :
    d = n%10
    print(d)
    n =n // 10