# built-in modules
import sys
sys.path.append('..')

# basic import
import MyModules.PyModule
MyModules.PyModule.sayHelloModule("John Doe")

print(" ")

# import with alias
import MyModules.PyModule as MyMPM
MyMPM.math(10, 10, "*")

print(" ")

# import from module
from MyModules.PyModule import person, fruit
print(f"Nama: {person['name']}")
print(f"City: {person['city']}")
print(f"Country: {person['country']}")

print(" ")

print(fruit[0])