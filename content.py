from ticket import Ticket

class ConcertTicket(Ticket):
    def _init_(self, customer_name_surname, date_str, seat_number, delivery_email, artist, venue):
        Ticket._init_(self, customer_name_surname, date_str, seat_number,)
        self.artist = artist
        self.delivery_email = delivery_email
        self.venue = venue

    def get_details(self):

        return (Ticket.get_details(self) +
                f" Artist: {self.artist}, Venue: {self.venue} Email: {self.delivery_email}," )

    def _str_(self):
        return f"Buyer: {self.customer_name_surname}, date: {self.date}, place: {self.seat_number}, Artist: {self.artist}, Email: {self.delivery_email}, City: {self.venue}"
