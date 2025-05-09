from ticket import Ticket

class FootballTicket(Ticket):
    def _init_(self, customer_name_surname, date_str, seat_number, match_name, sector,):
        Ticket._init_(self, customer_name_surname, date_str, seat_number, )
        self.match_name = match_name
        self.sector = sector

    def get_details(self):
        return Ticket.get_details(self) + f", Match: {self.match_name}"

    def _str_(self):
        return f"Sport Ticket: {self.customer_name_surname} | Game: {self.match_name} on {self.date}, Seat: {self.seat_number}, Sector: {self.sector}"
