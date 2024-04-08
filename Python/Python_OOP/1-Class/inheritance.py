class Person:
    name = "John Doe Jane"
    hobby = "fishing"
    message = "This is methof from parent class"

    def sayYourHobby(self):
        print(f"Hello my name {self.name}, my hobby is {self.hobby}")


class Budi(Person):
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby

    def myData(self):
        print(f"Nama: {self.name}")
        print(f"Hobby: {self.hobby}")


budi = Budi("Budi", "Fishing")
budi.myData()

print(budi.message)