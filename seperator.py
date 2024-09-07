str = "2,5,4,3,6"

new = ""

for i in range(len(str)):
    if str[i] == ",":
        continue
    else:
        new = new + str[i]

print(new)

news = str.split(",")

news.sort()

str2 =",".join(news)

print(str2)

