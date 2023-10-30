class User:
    def __init__(self, first_name, last_name, user_age, user_location):
        self.fname = first_name
        self.lname = last_name
        self.age = user_age
        self.locatin = user_location
    
    def describe_user(self):
        print(f'Name: {self.fname} / Last name: {self.lname} / Age: {self.age} / Location: {self.locatin}\n')

    def greet_user(self):
        print(f'Hello, {self.fname}, nice to see you!')

user1 = User('Vova', 'Shkv', '29', 'Vyshneve')
user2 = User('Vlad', 'Vdovitsa', '27', 'Kyiv')

user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()
