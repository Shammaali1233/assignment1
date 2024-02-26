from user import User


class GateAgent(User):
    def __init__(self, name: str, phone: str, email: str, age: int, airport: str, access_level: int, working_gate: int):
        super().__init__(name, phone, email, age)

        self.airport = airport
        self.access_level = access_level
        self.working_gate = working_gate

    def verify_ticket(self, ticket_id: int):
        # This function should return the details about ticket for given id.
        # Then gate agent can verify those details with user ticket.
        pass

    def set_airport(self, airport: str):
        self.airport = airport

    def get_airport(self):
        return self.airport

    def set_access_level(self, access_level: int):
        self.access_level = access_level

    def get_access_level(self):
        return self.access_level

    def set_working_gate(self, working_gate: int):
        self.working_gate = working_gate

    def get_working_gate(self):
        return self.working_gate
