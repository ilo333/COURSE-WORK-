from ticket import Ticket


class MovieTicket(Ticket):
    def _init_(self, customer_name_surname, date_str, seat_number, movie_title):

        Ticket._init_(self, customer_name_surname, date_str, seat_number)

        self.movie_title = movie_title

    def get_details(self):

        base = Ticket.get_details(self)
        return f"{base}, Movie: {self.movie_title}"

    def _str_(self):

        return f"MovieTicket for {self.customer_name_surname} to watch '{self.movie_title}' on {self.date} at seat {self.seat_number}"
