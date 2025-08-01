# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

class train:
    def __init__(self):
        
        self.booked=int(input("Enter the number of tickets to be booked: "))
        self.train_name="mas to chz"
        self.tickets_available=5
        self.fare_each=456
        self.available_seats=5
        
    def book_ticket(self):
        if self.booked>0:
            if self.booked>4:
                print("You can only book 4 tickets at once")
                return
            elif self.booked<=0:
                print("Please enter the appropriate number of tickets")
                return
            else:
                if  self.available_seats>=self.booked:
                    print("Tickets booked")
                else:
                    print("No tickets left")
        self.available_seats-=self.booked

    def get_status(self):
        if self.booked>4:
                return
        elif self.booked<=0:
            return
        else:
            print(f"the number of available seats: {self.available_seats}")
                    
    def fare_information(self):
        if self.booked>4:
                return
        elif self.booked<=0:
                return
        else:
            print(f"The total fare to be paid is: {self.booked*self.fare_each}")



get_info=train()

get_info.book_ticket()
get_info.get_status()
get_info.fare_information()


