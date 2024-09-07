from classes import User,Student

user1 = User('John', 26)
user2 = User('Jane', 28)
stud1 = Student("Vishwa",19,100)

print(User.user_count)

user1.register()
user2.login()

stud1.register()