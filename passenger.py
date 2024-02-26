from user import User


class Passenger(User):

    def __init__(self, name: str, phone: str, email:str, age: int, special_needs: bool, passport_number: str):
        super().__init__(name, phone, email, age)

        self.special_needs = special_needs
        self.passport_number = passport_number

    def get_id(self):
        return self.id

    def get_my_tickets(self):
        # This should search for this passenger id in the system and return
        # the ticket list for this passenger id.
        pass

    def set_special_needs(self, special_needs):
        self.special_needs = special_needs

    def get_special_needs(self):
        return self.special_needs

    def set_passport_number(self, passport_number):
        self.passport_number = passport_number

    def get_passport_number(self):
        return self.passport_number
