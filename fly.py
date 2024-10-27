class Flight():
    #method to create new flyht with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    #method to add a passenger to the flight
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    #Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
    

#Create a new flight with 0=up to 3 passengeres
flight = Flight(3)

#     Create a list of people
people = ["Harry", "Ron", "Hermione", "Ginny"]

# Attemp to add each person in the list to a flight
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
        