from operations import add_customer, add_device
from billing import generate_invoice
from gui import launch_gui

def menu():
    while True:
        print("\n--- RepairMate ---")
        print("1. Add Customer")
        print("2. Add Device")
        print("3. Generate Invoice")
        print("4. Launch GUI")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_device()
        elif choice == "3":
            generate_invoice()
        elif choice == "4":
            launch_gui()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

menu()
launch_gui()