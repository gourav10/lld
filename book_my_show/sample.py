"""
2. Design a Movie ticket booking system like BookMyShow
Problem statement and Machine coding practice link: https://codezym.com/question/10

In this question, core functionalities will include:

adding new cinema halls and new shows in those cinema halls.
Users can also book and cancel tickets.
Users should also be able to list all cinemas in a city which are displaying a particular movie.
Also they should be able to fetch list of all shows in a cinema hall which are displaying a particular movie.
Classes implementing last two search features need to updated whenever a new show gets added, so that they can update their respective lists.

We use observer design pattern to send new show added updates to the search movie/show classes.

0. Cinema Hall
 - shows
 - seats
 - available
 - timings
2. Shows
    - show_id
    - show name
3. User
    + book 
    + cancel
    + searchMovieByCity - show all the cinema halls
    + fetchAllShowsin Cinema Hall

4. Ticket:
    - ticket

"""


class Show:
    def __init__(self,show_name):
        self.show_name = show_name
    
class Ticket:
    def __init__(self,show_id,hall,user_id):
        self.user_id = user_id
        self.show_id = show_id
        self.hall = hall 
       
class CinemaHall:
    def __init__(self,name):
        self.name = name
        self.seats = 100
        self.bms_core = BookMyShow()
        pass

    def addShows(self,show:Show):
        self.bms_core.addShow(self,show)

    def isSeatAvailable(self):
        if len(self.seats):
            return True
        return False
    
    def update(self,action,ticket:Ticket):
        try:
            if action == "BOOK":
                if self.seats>0:
                    self.seats-=1
                    print(f" {self.seats} seats left")
            else:
                self.seats = self.seats+1 if self.seats<100 else 100
                print(f"{self.seats} seats left")
        except:
            return "Failed to book ticket"
    
class User:

    def __init__(self,user_name):
        self.user_name = user_name
        self.tickets = []
        self.bms_core = BookMyShow()
        pass

    def book(self,show,hall):
        self.bms_core.bookTicket(self,show,hall)
    
    def cancel(self,ticket):
        self.bms_core.cancelTicket(self,ticket)

    def search_show_by_hall(self,show_name):
        self.bms_core.search_show_by_city(show_name)

class BookMyShow:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(BookMyShow, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.users = {}
        self.halls = {}
        self.shows = {}
        pass
    
    def addShow(self,hall,show):
        if hall in self.halls:
            self.halls[hall].append(show)
            self.shows[show].append(hall)
        else:
            self.halls[hall] = [show]

    def bookTicket(self,user:User,show:Show,hall:CinemaHall):
        try:
            if show in self.halls[hall]:
                ticket = Ticket(show.show_name,hall.name,user.user_name)
                hall.update("BOOK",ticket)
                return ticket
        except:
            return print("Failed to book!")


    def cancelTicket(self,user:User,ticket:Ticket):
        try:
            for hall in self.halls:
                if hall.name == ticket.hall:
                    return hall.update("CANCEL", ticket)
        except:
            return print("Failed to cancel")

    def search_show_by_city(self, movie):
        result = []
        for hall in self.halls:
            for show in self.halls[hall].shows:
                if show.show_name == movie:
                    result.append(hall.name)
        
        return result
    
    def search_show_by_cinema_hall(self,cinema_hall:CinemaHall):
        if not cinema_hall in self.halls:
            return Exception("Cinema Hall not found!")

        result = []
        for show in cinema_hall.shows:
            result.append(show.show_name)


if __name__ == "__main__":
    
    user1 = User("Gourav")
    user2 = User("Neelesh")
    user3 = User("Mayan")

    show1 = Show("Avengers")
    show2 = Show("Inception")
    show3 = Show("Annabelle")

    hall1 = CinemaHall("AMC")
    hall1.addShows(show1)
    hall1.addShows(show2)
    hall1.addShows(show3)
    tick = user1.book(show1,hall1)
    # print(user1.cancel())

    
        



    
