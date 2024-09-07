# with open("myfile.txt") as files:
#     print(files.read())
#     # files.write("I will become an ai enginner")
#
# try:
#     with open("C:\\Users\\VishwanathRR\\OneDrive\\Desktop\\hi.txt", "a") as f:
#         print(f.write("\nMake it fast"))
# except PermissionError as e:
#     print(e)

with open("myfile.txt") as file:
    string = file.read()
    new_string = string.replace("cows","ducks")
    new_str = new_string.replace("moo","quack")
    print(new_str)
    with open("myfile.txt","a") as file:
        file.write("\n\n"+new_str)

