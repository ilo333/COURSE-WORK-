from ticket import Ticket

class FlightTicket(Ticket):
    def _init_(self, customer_name_surname, date_str, seat_number, gate, destination):
        Ticket._init_(self, customer_name_surname, date_str, seat_number)
        self.gate = gate
        self.destination = destination
    def get_details(self):
           return Ticket.get_details(self) + f", Airport Code: {self.gate}"

    def _str_(self):
        return f"Buyer: {self.customer_name_surname}, date: {self.date}, place: {self.seat_number}, Airport Code: {self.gate}, City: {self.destination}"
