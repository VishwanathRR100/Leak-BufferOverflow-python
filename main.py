print("hello world")

print(12 << 2)

string = "Vishwanath.R.R"

print(string[1:8:2])

print(string[::2])

x = slice(5, 10)

print(string[x])

str = "Happy"

i = -1
string = ""
while abs(i) <= len(str):
    string = str[i] + string
    print(string)
    i -= 1
