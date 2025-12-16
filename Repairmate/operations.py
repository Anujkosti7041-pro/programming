from models import Customer, Device

customers = []

def add_customer():
    cid = input("Customer ID: ")
    name = input("Name: ")
    phone = input("Phone: ")
    customers.append(Customer(cid, name, phone))
    print("Customer added")

def add_device():
    cid = input("Enter Customer ID: ")
    for cust in customers:
        if cust.cid == cid:
            model = input("Device Model: ")
            issue = input("Issue: ")
            cust.add_device(Device(model, issue))
            print("Device added")
            return
    print("Customer not found")
