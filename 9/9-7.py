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

class Admin(User):
    def __init__(self, first_name, last_name, user_age, user_location):
        super().__init__(first_name, last_name, user_age, user_location)
        self.privileges = ['can add post', 'can delete post', 'can bar user']

    def show_privileges(self):
        print(f'Administrator have next privileges: {self.privileges}')

admin = Admin('Vova', 'Shkvarun', '29', 'Vyshnev')
admin.show_privileges()
