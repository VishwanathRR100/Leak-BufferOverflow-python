class User:
    user_count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        User.user_count += 1
    def register(self):
        print('User {} is registering...'.format(self.name))
    def login(self):
        print('User {} is logging... in'.format(self.name))

class Student(User):
    student_count = 0
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score
        Student.student_count += 1
    def register(self):
        print('Welcome student {} ...'.format(self.name))