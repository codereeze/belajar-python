class Person:
    def __init__(self, firstname, lastname, address, hobby, age):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.hobby = hobby
        self.age = age
        self.printMyBio()

    def printMyBio(self): 
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Address: {self.address}")
        print(f"Hobby: {self.hobby}")
        print(f"Age: {self.age}")

person = Person("Jane", "Doe", "Singapore city", "Badminton", 18)


