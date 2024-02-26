class Flight:
    id = 0  # Static attribute to generate a unique id for each flight object.

    def __init__(self, airline: str, seats: int, registration_number: int, model: str):
        Flight.id += 1
        self.id = Flight.id

        self.airline = airline
        self.seats = seats
        self.registration_number = registration_number
        self.model = model

    def get_id(self):
        return self.id

    def set_airline(self, airline: str):
        self.airline = airline

    def get_airline(self):
        return self.airline

    def set_seats(self, seats: int):
        self.seats = seats

    def get_seats(self):
        return self.seats

    def set_registration_number(self, registration_number: int):
        self.registration_number = registration_number

    def get_registration_number(self):
        return self.registration_number

    def set_model(self, model: str):
        self.model = model

    def get_model(self):
        return self.model
