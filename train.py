from ticket import Ticket

class TrainDestination(Ticket):
    def _init_(self, customer_name_surname, date_str, seat_number, destination, coach_class):
        Ticket._init_(self, customer_name_surname, date_str, seat_number)
        self.destination = destination
        self.coach_class = coach_class

    def get_details(self):
        base = Ticket.get_details(self)
        return f"{base}, Destination: {self.destination}, Class: {self.coach_class}"

    def _str_(self):
        return (f"Train ticket for {self.customer_name} to {self.destination} "
                f"on {self.date}, Seat: {self.seat_number}, Class: {self.coach_class}")
