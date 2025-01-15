comunication_queue = []

class Customer:
    def __init__(self, name, dob, id_number):
        self.name = name
        self.dob = dob
        self.id_number = id_number

def place_order(self, store_name, product_name):
    event ={"event_type":"place_order","payload":{"customer_id":self.id_number, "customer_name":self.name, "customer_dob":self.dob}}
    comunication_queue.append(event)
    print(f"Order request created for {self.name.")

class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location
