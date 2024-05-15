import inspect

class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def greet(self):
        return f"Hello, my name is {self.name}"

    def add_value(self, amount):
        self.value += amount
        return self.value

# Membuat instance dari kelas MyClass
obj = MyClass('Alice', 42)

# Fungsi untuk memeriksa properti dan metode
def inspect_class(obj):
    attributes = dir(obj)
    properties = []
    methods = []

    for attr in attributes:
        if not attr.startswith('__'):
            attr_value = getattr(obj, attr)
            if inspect.ismethod(attr_value) or inspect.isfunction(attr_value):
                methods.append(attr)
            else:
                properties.append(attr)

    return properties, methods

# Memanggil fungsi dan mencetak hasilnya
properties, methods = inspect_class(obj)
print("Properties:", properties)
print("Methods:", methods)