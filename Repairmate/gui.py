import tkinter as tk
from tkinter import messagebox

# import functions from other files
from operations import add_customer, add_device
from billing import generate_invoice


def launch_gui():
    root = tk.Tk()
    root.title("RepairMate - TechFix Hub")
    root.geometry("350x300")

    title = tk.Label(
        root,
        text="RepairMate System",
        font=("Arial", 16, "bold")
    )
    title.pack(pady=10)

    # -------------------------------
    # Button functions
    # -------------------------------
    def add_customer_gui():
        add_customer()
        messagebox.showinfo("Success", "Customer added (console input)")

    def add_device_gui():
        add_device()
        messagebox.showinfo("Success", "Device added (console input)")

    def generate_invoice_gui():
        generate_invoice()
        messagebox.showinfo("Success", "Invoice saved to file")

    btn1 = tk.Button(root, text="Add Customer", width=25, command=add_customer_gui)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Add Device", width=25, command=add_device_gui)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Generate Invoice", width=25, command=generate_invoice_gui)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Exit", width=25, command=root.destroy)
    btn4.pack(pady=20)

    root.mainloop()
