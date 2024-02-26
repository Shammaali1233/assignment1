class User:
    id = 0  # Static attribute to generate a unique id for each user object.

    def __init__(self, name: str, phone: str, email: str, age: int):
        User.id += 1
        self.id = User.id

        self.name = name
        self.phone = phone
        self.email = email
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

