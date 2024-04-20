class Star_Cinema:

    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seats = []
        for _ in range(self.__rows):
            row = []
            for _ in range(self.__cols):
                row.append(0)
            seats.append(row)
        self.__seats[id] = seats
        
    def book_seats(self, id, booking_seats):
        if id not in self.__seats:
            print("invalid show id")
            return
        for row, col in booking_seats:
            if row <= self.__rows and col <= self.__cols:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                else:
                    print(f"Seat ({row}, {col}) is already booked in show {id} in Hall {self.__hall_no}.")
            else:
                print(f"Seat ({row}, {col}) is not a valid seat in show {id} in Hall {self.__hall_no}.")
                
                
    def view_show_list(self):
        print("running show:")
        for show in self.__show_list:
            print(f'id: {show[0]}, movie_name: {show[1]}, time: {show[2]}')
                
    def available_seats(self, id):
        if id not in self.__seats:
            print("invalid show id")
            return
        print(f'available seats in show {id} in hall {self.__hall_no}')
        for row in self.__seats[id]:
            for seat in row:
                print(seat, end = " ")
            print()

cinema = Star_Cinema()
hall = Hall(4,4,1)
cinema.entry_hall(hall)

hall.entry_show("103", "Avenger", "10:00 AM")
hall.entry_show("104", "SpiderMan", "2:00 PM")

hall.view_show_list()
print()
hall.book_seats("103", [(1,1),(2,3)])
hall.available_seats("103")
print()
hall.book_seats("104", [(3,2)])
hall.available_seats("104")