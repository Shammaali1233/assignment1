from datetime import datetime


class Ticket:
    id = 0  # Static attribute to generate a unique id for each ticket object.

    def __init__(self,
                 flight_id: int,
                 gate: int,
                 date: datetime.date,
                 boarding_time: datetime.time,
                 departure_time: datetime.time,
                 arrival_time: datetime.time,
                 seat: str,
                 origin: str,
                 destination: str,
                 therminal: int,
                 seat_class: str):
        Ticket.id += 1
        self.id = Ticket.id
        self.flight_id = flight_id
        self.gate = gate
        self.date = date
        self.boarding_time = boarding_time
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seat = seat
        self.origin = origin
        self.destination = destination
        self.therminal = therminal
        self.seat_class = seat_class
        self.passenger_id = None

    def get_details(self):
        return {
            "ticket_id": self.id,
            "passenger_id": self.passenger_id,
            "flight_id": self.flight_id,
            "gate": self.gate,
            "date": self.date,
            "boarding_time": self.boarding_time,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "seat": self.seat,
            "origin": self.origin,
            "destination": self.destination,
            "therminal": self.therminal,
            "seat_class": self.seat_class
        }

    def buy(self, passenger_id: int):
        self.passenger_id = passenger_id

    def get_id(self):
        return self.id

    def set_passenger_id(self, passenger_id: int):
        self.passenger_id = passenger_id

    def get_passenger_id(self):
        return self.passenger_id

    def set_flight_id(self, flight_id: int):
        self.flight_id = flight_id

    def get_flight_id(self):
        return self.flight_id

    def set_gate(self, gate: int):
        self.gate = gate

    def get_gate(self):
        return self.gate

    def set_date(self, date: datetime.date):
        self.date = date

    def get_date(self):
        return self.date

    def set_time(self, time: datetime.time):
        self.time = time

    def get_time(self):
        return self.time

    def set_seat(self, seat: str):
        self.seat = seat

    def get_seat(self):
        return self.seat

    def set_origin(self, origin: str):
        self.origin = origin

    def get_origin(self):
        return self.origin

    def set_destination(self, destination: str):
        self.destination = destination

    def get_destination(self):
        return self.destination

    def set_therminal(self, therminal: int):
        self.therminal = therminal

    def get_therminal(self):
        return self.therminal

    def set_seat_class(self, seat_class: str):
        self.seat_class = seat_class

    def get_seat_class(self):
        return self.seat_class
