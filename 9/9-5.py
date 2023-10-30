class User:
    def __init__(self, first_name, last_name, user_age, user_location):
        self.fname = first_name
        self.lname = last_name
        self.age = user_age
        self.locatin = user_location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f'Name: {self.fname} / Last name: {self.lname} / Age: {self.age} / Location: {self.locatin}\n')

    def greet_user(self):
        print(f'Hello, {self.fname}, nice to see you!')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    


user1 = User('Vova', 'Shkv', '29', 'Vyshneve')
#user2 = User('Vlad', 'Vdovitsa', '27', 'Kyiv')

user1.greet_user()
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f'attempts - {user1.login_attempts}')
user1.reset_login_attempts()
print(f'Reset attempts, counter: {user1.login_attempts}')
#user2.greet_user()
#user2.describe_user()