from ticket import Ticket
from passenger import Passenger
from flight import Flight
from datetime import date, time

# Creating a flight object.
flight = Flight("srilankan",
                100,
                1234,
                "boeing")

# Creating a passenger object.
passenger = Passenger("alex",
                      "+945789486",
                      "alex@gmail.com",
                      25,
                      False,
                      "sl-87545")

# Creating a ticket object.
ticket = Ticket(flight.get_id(),
                1,
                date(2024, 2, 13),
                time(6, 50),
                time(7, 26),
                time(5, 45),
                "K-56",
                "Chicago ORD",
                "New York JFK",
                2,
                "First Class"
                )

# Passenger buys a ticket.
ticket.buy(passenger.get_id())

# Sample ticket detail accessing. This function will used buy the gate agent.
print(ticket.get_details())
