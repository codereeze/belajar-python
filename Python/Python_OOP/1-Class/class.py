class Person:
    # this is property
    firstname = "John"
    lastname = "Doe"
    address = "New York, US"
    hobby = "Reading"
    age = 30


    # this is method
    def printMyBio(self):
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Address: {self.address}")
        print(f"Hobby: {self.hobby}")
        print(f"Age: {self.age}")

person = Person()
person.printMyBio()


