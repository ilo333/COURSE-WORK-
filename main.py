from manager import TicketManager
from movie import MovieTicket
from train import TrainDestination
from plane import FlightTicket
from concert import ConcertTicket
from football import FootballTicket

def main():
    manager = TicketManager()

    manager.add_ticket(MovieTicket("bayram Gagasilov", "2025-05-10", "A1", "john wick"))
    manager.add_ticket(TrainDestination("ravan Kardeshow", "2025-06-01", "12B", "Tbilisi","first_class"))
    manager.add_ticket(MovieTicket("ruslan gaga" , "2024-05-01", "A12", "asdhasjkdhaskjjas",))
    manager.add_ticket(FlightTicket("ilyas ilyas", "2029-11-03", "F33", "C5099", "Kutaisi"))
    manager.add_ticket(ConcertTicket("anar Badalov","2020-01-31","q132","anar@gmail.com","INNA","Paris"))
    manager.add_ticket(FootballTicket("anar baladov" , "2028-12-30", "t88","barcelona-vs-inter_milane","5",))

    print("\n=== All Tickets ===")
    manager.show_all()

    print("\n=== Sorted by Date ===")
    manager.sort_by_date()
    manager.show_all()

    print("\n=== Filter by Name: anar ===")
    for t in manager.filter_by_name("anar"):
        print(t.get_details())

if _name_ == "_main_":
    main()
