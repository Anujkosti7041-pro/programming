def generate_invoice():
    try:
        service = float(input("Service Cost: "))
        parts = float(input("Parts Cost: "))
        tax = 0.18
        total = service + parts + (service + parts) * tax

        with open("data/invoices.txt", "a") as f:
            f.write(f"Total Bill: {total}\n")

        print("Invoice saved")

    except ValueError:
        print("Invalid input")
