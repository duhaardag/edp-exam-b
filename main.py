communication_queue = []

class Customer:
    def __init__(self, name, dob, id_number):
        self.name = name
        self.dob = dob
        self.id_number = id_number

    def place_order(self, store_name, product_name):
        event = {
            "event_type": "place_order",
            "payload": {"customer_id": self.id_number,"customer_name": self.name,"customer_dob": self.dob,"store_name": store_name,"product_name": product_name}}
        communication_queue.append(event)
        print(f"Order request created for {self.name} at {store_name} for {product_name}.")

class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def handle_order(self):
        if communication_queue:
            order = communication_queue.pop(0)
            payload = order["payload"]
            print(f"Received order from {payload['customer_name']} (ID: {payload['customer_id']}, DOB: {payload['customer_dob']}) at {payload['store_name']} for {payload['product_name']}.")
        else:
            print("No orders to handle.")


customer1 = Customer("Duha", "03.08.2005", "411672")
customer2 = Customer("Lara", "09.09.2007", "465205")


store = Store("Lidl", "Warsaw")

customer1.place_order("Lidl", "Apples")
customer2.place_order("Lidl", "Bananas")

store.handle_order()

