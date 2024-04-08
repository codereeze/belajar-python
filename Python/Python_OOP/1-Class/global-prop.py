class Person:
    global firstname
    global lastname
    global address
    global hobby
    global age

    def __init__(self, firstname, lastname, address, hobby, age):
        firstname = firstname
        lastname = lastname
        address = address
        hobby = hobby
        age = age
        self.printMyBio()

    def printMyBio(self): 
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Address: {self.address}")
        print(f"Hobby: {self.hobby}")
        print(f"Age: {self.age}")

person = Person("Jane", "Doe", "Singapore city", "Badminton", 18)
