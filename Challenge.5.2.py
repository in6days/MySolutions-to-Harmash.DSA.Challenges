#تراكيب البيانات - التحدي الثاني

class Person:
    __id_counter = 0

    def __init__(self, name, phone, gender):
        Person.__id_counter += 1
        self.id = Person.__id_counter
        self.name = name
        self.phone = phone
        self.gender = gender

class Client(Person):

    def __init__(self, name, phone, gender, email):
        super().__init__(name, phone, gender)
        self.email = email

class Employee(Person):

    def __init__(self, name, phone, gender, salary, working_time):
        super().__init__(name, phone, gender)
        self.salary = salary
        self.working_time = working_time

class Product:

    __id_counter = 0

    def __init__(self, name, price):
        Product.__id_counter += 1
        self.id = Product.__id_counter
        self.name = name
        self.price = price

class Order:

    __id_counter = 0

    def __init__(self, date, is_paid, person, products):
        Order.__id_counter += 1
        self.id = Order.__id_counter
        self.date = date
        self.is_paid = is_paid
        self.person = person
        self.products = products

class Company:
    persons = []
    products = []
    orders = []

    def add_product(self, product):
        self.products.append(product)

    def add_person(self, person):
        self.persons.append(person)

    def add_order(self, order):
        self.orders.append(order)

    def remove_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                return
        print("Product with id", id, "is not found!")
        print("----------------------")

    def remove_person(self, id):
        for person in self.persons:
            if person.id == id:
                self.persons.remove(person)
                return
        print("Person with id", id, "is not found!")
        print("----------------------")

    def remove_order(self, id):
        for order in self.orders:
            if order.id == id:
                self.orders.remove(order)
                return
        print("Order with id", id, "is not found!")
        print("----------------------")

    def print_person_info(self, id):
        for person in self.persons:
            if person.id == id:
                print("Person with id", id, "info.")
                print("Name:", person.name)
                print("Phone:", person.phone)
                print("Gender", person.gender)

                if isinstance(person, Client):
                    print("Email:", person.email)

                elif isinstance(person, Employee):
                    print("Salary:", person.salary)
                    print("Working time", person.working_time)

                # بعدها سيتم طباعة خط و الخروج من الدالة
                print("----------------------")
                return
        print("Person with id", id, "is not found!")
        print("----------------------")

    def print_product_details(self, id):
        for product in self.products:
            if product.id == id:
                print("Product with id", id, "info.")
                print("Name:", product.name)
                print("Price:", str(product.price) + "$")
                print("----------------------")
                return
        print("Product with id", id, "is not found!")
        print("----------------------")

    def print_order_details(self, id):
        total_sum = 0
        for order in self.orders:
            if order.id == id:
                print("Order with id", id, "details.")
                print("Date:", order.date)
                print("Is paid:", "yes" if order.is_paid else "no")
                print("Ordered by:", order.person.name)
                print("Products")

                for product in order.products:
                    total_sum += product.price
                    print("- " + product.name + ": " + str(product.price) + "$")

                print("Total Price: " + str(total_sum) + "$")
                print("----------------------")
                return
        print("Order with id", id, "is not found!")
        print("----------------------")

    def print_person_orders(self, id):
        is_person_exist = False
        for person in self.persons:
            if person.id == id:
                is_person_exist = True
                break

        if not is_person_exist:
            print("Person with id", id, "is not found!")
            print("----------------------")
            return
        print("All orders made by person with id " + str(id) + ":")
        for order in self.orders:
            if order.person.id == id:
                print("> Order: #" + str(order.id))
                print("  Date:", order.date)
                print("  Is paid:", "yes" if order.is_paid else "no")
                print("  Ordered by:", order.person.name)
                print("  Products")
                total_sum = 0
                for product in order.products:
                    total_sum += product.price
                    print("  - " + product.name + ": " + str(product.price) + "$")
                print("  Total Price: " + str(total_sum) + "$")
        print("----------------------")

#مثال

person1 = Client("Mhamad", "+96170123456", "Male", "mhamad@example.com")
person2 = Employee("Nadine", "+9631249392", "Female", 800, "8:00 AM to 3:00 PM")

product1 = Product("Keyboard", 15)
product2 = Product("Camera", 45)
product3 = Product("HDD 1TB", 70)
product4 = Product("SSD 1TB", 274.66)
product5 = Product("Mouse", 8)
product6 = Product("Table", 44.55)

order1 = Order("2020-1-1", True, person1, [product1, product2, product3])
order2 = Order("2020-2-7", True, person1, [product4])
order3 = Order("2020-5-4", False, person2, [product5, product6])

company = Company()

company.add_person(person1)
company.add_person(person2)

company.add_product(product1)
company.add_product(product2)
company.add_product(product3)
company.add_product(product4)
company.add_product(product5)
company.add_product(product6)

company.add_order(order1)
company.add_order(order2)
company.add_order(order3)

company.print_person_info(1)
company.print_person_info(2)

company.print_product_details(1)
company.print_product_details(2)
company.print_product_details(3)
company.print_product_details(4)
company.print_product_details(5)
company.print_product_details(6)

company.print_person_orders(1)
company.print_person_orders(2)

company.remove_order(1)
company.print_order_details(1)
company.print_person_orders(1)

#انتهى