class User:
    def log(self):
        print("Users")


class Teacher(User):
    def log(self):
        print("Teacher: ")


class Customer(User):

    def log(self):
        print("Customer: ")

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def update_membership(self, new_membership):
        print("Calculating costs")
        self.membership_type = new_membership

    def read_customer():
        print("Reading customer from DB")

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    __hash__ = None

    __repr__ = __str__


# c = Customer("Sam", "Gold")
# print(c.name, c.membership_type)
# c2 = Customer("Caleb", "Bronze")
# print(c2.name, c2.membership_type)

users = [Customer("Sam", "Gold"), Customer("Caleb", "Bronze"), Teacher()]


# print(customers[1])
# customers[1].update_membership("Gold")
# print(customers[1].membership_type)


# # //static methods
# Customer.read_customer()
# Customer.print_all_customers(customers)

# print(customers[0] == customers[1])


# data = {customers[0]}

# del customers[0].name
for user in users:
    user.log()
