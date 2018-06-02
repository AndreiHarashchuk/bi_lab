class Customer(object):

    def __init__(self, name, credit_card, account_amount):
        self.name = name
        self.credit_card = credit_card
        self.account_amount = account_amount

    def show(self):
        print()
        print(self.name)
        print(self.credit_card, ":", self.account_amount, "$")


class Room(object):

    def __init__(self, number, cost):
        self.number = number
        self.cost = cost
        self.customer_name = ""

    def show(self):
        print()
        print(self.number)
        print(self.cost, "$")
        print(self.customer_name)

    def assign_room(self, customer, number_of_days):
        print()
        print("Assigning room", self.number, "to", customer.name)
        print()
        if customer.account_amount < self.cost * number_of_days:
            print()
            print("Insufficient funds!")
            print()
        else:
            self.customer_name = customer.name
            customer.account_amount -= self.cost * number_of_days
            print("Success!")


customers = list()
customers.append(Customer("Vitya", "1234 5678 8765 4321", 5000))
customers.append(Customer("Tanya", "9876 5432 2345 6789", 5000))
customers.append(Customer("Vanya", "1010 0101 1010 0101", 5000))
rooms = list()
rooms.append(Room("567A", 56.20))
rooms.append(Room("123B", 10))
rooms.append(Room("02C", 350))
for customer in customers:
    for room in rooms:
        if not room.customer_name:
            room.show()
            if input("Does customer want this room? (y/n) ") == "y":
                room.assign_room(customer, int(input("Number of days: ")))
                continue
