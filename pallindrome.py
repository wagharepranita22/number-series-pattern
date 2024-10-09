# # print all digits of a number on different lines
# solution 1
# n = int(input("Give n Number  : "))
# copy = n
# a = ""
# while n != 0:
#     d = n%10
#     a += str(d)
#     n =n // 10
#
# a = int(a)
# if a == copy:
#     print("number is pallindrome")
# else:
#     print("number is not pallindrome")

# solution 2
n = int(input("Give n Number  : "))
copy = n
a =0
while n != 0:
    d = n%10
    a =a*10+d
    n =n // 10

a = int(a)
if a == copy:
    print("number is pallindrome")
else:
    print("number is not pallindrome")