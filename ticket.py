import datetime


class Ticket:
    def _init_(self,customer_name_surname , date_str, seat_number):
        self.customer_name_surname = customer_name_surname
        self.seat_number = seat_number


        try:
            self.date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Incorrect date format! Must be in YYYY-MM-DD format.")

    def get_details(self):
        return f"Buyer: {self.customer_name_surname}, date: {self.date}, place: {self.seat_number}"

    def _str_(self):
        return f"ticket for {self.customer_name_surname} in {self.date}"
