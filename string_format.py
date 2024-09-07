name = "Vishwanath"
like1 = "Bananas"
like2 = "Apples"

text = "{} likes {} and {}"
print(text.format(name,like1, like2))

print("hello my name is {name}".format(name="Vishwanath"))
print("pi value is {val:.2f}".format(val=3.14569))  # rounding off
print("*******{msg:^20}********".format(msg="Welcome"))  # padding ^ - both left and right , > for left , < for right
# print("binary value of  {val} is {val:b}".format(val="hello")) # x- hexadec , o - octet , E - scintific notation
print("value is {val:,}".format(val=100000000))
print("hi {msg:>10}".format(msg=100))

arr = [1,2,3,4]

arr.reverse()

print(arr)
