class TicketManager:
    def _init_(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def show_all(self):
        for ticket in self.tickets:
            print(ticket.get_details())

    def sort_by_date(self):
        self.tickets.sort(key=self.get_ticket_date)

    def get_ticket_date(self, ticket):
        return ticket.date

    def filter_by_name(self, name):
        filtered_tickets = []

        for i in range(len(self.tickets)):
            ticket = self.tickets[i]

            if name.lower() in ticket.customer_name_surname.lower():
                filtered_tickets.append(ticket)

        return filtered_tickets
