import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime

customers = []          
orders = []             
users = [
    {"username": "admin", "password": "admin123", "role": "Admin"},
    {"username": "tech", "password": "tech123", "role": "Technician"},
]
current_user = {"username": None, "role": None}

<<<<<<< HEAD
class RepairMateException(Exception):
    
    pass
=======

def show_login(root):
>>>>>>> 3aa298264ead45f7c4e5099e1d2673533bcb40d8


    root.title("RepairMate - Login")
    root.geometry("400x300")

    frame = ttk.Frame(root, padding="20")
    frame.pack(expand=True)

    ttk.Label(frame, text="RepairMate Login", font=("Arial", 16, "bold")).grid(
        row=0, column=0, columnspan=2, pady=20
    )

    ttk.Label(frame, text="Username:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    username_entry = ttk.Entry(frame, width=20)
    username_entry.grid(row=1, column=1, pady=5)

    ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    password_entry = ttk.Entry(frame, width=20, show="*")
    password_entry.grid(row=2, column=1, pady=5)

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password required")
            return

        user = None
        for u in users:
            if u["username"] == username and u["password"] == password:
                user = u
                break

        if user is None:
            messagebox.showerror("Error", "Invalid credentials")
            return

        current_user["username"] = user["username"]
        current_user["role"] = user["role"]
        show_main_app(root)

    ttk.Button(frame, text="Login", command=login).grid(
        row=3, column=0, columnspan=2, pady=20
    )

    info_text = "Default users:\nAdmin: admin/admin123\nTechnician: tech/tech123"
    ttk.Label(frame, text=info_text, font=("Arial", 8), foreground="gray").grid(
        row=4, column=0, columnspan=2
    )
    
def show_main_app(root):
    root.title(f"RepairMate - {current_user['role']}: {current_user['username']}")
    root.geometry("900x600")

    top = ttk.Frame(root)
    top.pack(side="top", fill="x", padx=5, pady=5)

    ttk.Label(
        top,
        text=f"Logged in as: {current_user['username']} ({current_user['role']})",
        font=("Arial", 10),
    ).pack(side="left")
    ttk.Button(top, text="Logout", command=lambda: show_login(root)).pack(side="right")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=5, pady=5)

    role = current_user["role"]
    if role == "Admin":
        notebook.add(create_customer_tab(notebook), text="Customers")
        notebook.add(create_order_tab(notebook), text="Repair Orders")
        notebook.add(create_billing_tab(notebook), text="Billing")
        notebook.add(create_reports_tab(notebook), text="Reports")
    else:
        notebook.add(create_order_tab(notebook), text="Repair Orders")
        notebook.add(create_reports_tab(notebook), text="Reports")


def create_customer_tab(parent):
    frame = ttk.Frame(parent)

    form = ttk.LabelFrame(frame, text="Customer Information", padding="10")
    form.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    name_entry = ttk.Entry(form, width=30)
    name_entry.grid(row=0, column=1, pady=5)

    ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    email_entry = ttk.Entry(form, width=30)
    email_entry.grid(row=1, column=1, pady=5)

    ttk.Label(form, text="Phone:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    phone_entry = ttk.Entry(form, width=30)
    phone_entry.grid(row=2, column=1, pady=5)

    ttk.Label(form, text="Address:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    address_entry = ttk.Entry(form, width=30)
    address_entry.grid(row=3, column=1, pady=5)

    ttk.Label(form, text="Device Model:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    model_entry = ttk.Entry(form, width=30)
    model_entry.grid(row=4, column=1, pady=5)

    ttk.Label(form, text="Brand:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
    brand_entry = ttk.Entry(form, width=30)
    brand_entry.grid(row=5, column=1, pady=5)

    ttk.Label(form, text="Type:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
    type_entry = ttk.Entry(form, width=30)
    type_entry.grid(row=6, column=1, pady=5)

    list_frame = ttk.LabelFrame(frame, text="Customer List", padding="10")
    list_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    columns = ("ID", "Name", "Email", "Phone")
    tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    def refresh_list():
        tree.delete(*tree.get_children())
        for c in customers:
            tree.insert(
                "",
                "end",
                values=(c["id"], c["name"], c["email"], c["phone"]),
            )

    def save_customer():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()

        if not name or not email or not phone:
            messagebox.showerror("Error", "Name, email, and phone are required")
            return

        cid = f"C{len(customers) + 1:04d}"
        devices = []
        if model_entry.get().strip():
            devices.append(
                {
                    "id": "D0001",
                    "model": model_entry.get().strip(),
                    "brand": brand_entry.get().strip(),
                    "type": type_entry.get().strip(),
                }
            )

        customers.append(
            {
                "id": cid,
                "name": name,
                "email": email,
                "phone": phone,
                "address": address_entry.get().strip(),
                "devices": devices,
            }
        )

        messagebox.showinfo("Success", f"Customer {cid} created successfully!")

        for e in [
            name_entry,
            email_entry,
            phone_entry,
            address_entry,
            model_entry,
            brand_entry,
            type_entry,
        ]:
            e.delete(0, tk.END)

        refresh_list()

    ttk.Button(form, text="Save Customer", command=save_customer).grid(
        row=7, column=0, columnspan=2, pady=10
    )

    refresh_list()
    return frame

def create_order_tab(parent):
    frame = ttk.Frame(parent)

    form = ttk.LabelFrame(frame, text="New Repair Order", padding="10")
    form.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    ttk.Label(form, text="Customer ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    customer_combo = ttk.Combobox(form, width=28)
    customer_combo["values"] = [c["id"] for c in customers]
    customer_combo.grid(row=0, column=1, pady=5)

    ttk.Label(form, text="Device:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    device_combo = ttk.Combobox(form, width=28)
    device_combo.grid(row=1, column=1, pady=5)

    def update_devices(event):
        cid = customer_combo.get()
        for c in customers:
            if c["id"] == cid:
                device_combo["values"] = [
                    d["id"] + ": " + d["brand"] + " " + d["model"] for d in c["devices"]
                ]
                break

    customer_combo.bind("<<ComboboxSelected>>", update_devices)

    ttk.Label(form, text="Issue Description:").grid(
        row=2, column=0, sticky="ne", padx=5, pady=5
    )
    issue_text = tk.Text(form, width=30, height=5)
    issue_text.grid(row=2, column=1, pady=5)

    ttk.Label(form, text="Technician:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    tech_entry = ttk.Entry(form, width=30)
    tech_entry.insert(0, current_user["username"] or "")
    tech_entry.grid(row=3, column=1, pady=5)

    ttk.Label(form, text="Status:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    status_combo = ttk.Combobox(
        form, width=28, values=["Pending", "In Progress", "Completed", "Cancelled"]
    )
    status_combo.set("Pending")
    status_combo.grid(row=4, column=1, pady=5)

    ttk.Label(form, text="Service Cost:").grid(
        row=5, column=0, sticky="e", padx=5, pady=5
    )
    service_entry = ttk.Entry(form, width=30)
    service_entry.insert(0, "0")
    service_entry.grid(row=5, column=1, pady=5)

    ttk.Label(form, text="Parts Cost:").grid(
        row=6, column=0, sticky="e", padx=5, pady=5
    )
    parts_entry = ttk.Entry(form, width=30)
    parts_entry.insert(0, "0")
    parts_entry.grid(row=6, column=1, pady=5)

    list_frame = ttk.LabelFrame(frame, text="Repair Orders", padding="10")
    list_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    columns = ("Order ID", "Customer", "Status", "Technician")
    tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    def refresh_orders():
        tree.delete(*tree.get_children())
        for o in orders:
            tree.insert(
                "",
                "end",
                values=(o["id"], o["customer_id"], o["status"], o["technician"]),
            )

    def save_order():
        cid = customer_combo.get()
        device_info = device_combo.get()
        issue = issue_text.get("1.0", tk.END).strip()

        if not cid or not device_info or not issue:
            messagebox.showerror("Error", "Customer, device, and issue are required")
            return

        try:
            service_cost = float(service_entry.get())
            parts_cost = float(parts_entry.get())
        except Exception:
            messagebox.showerror("Error", "Costs must be numeric values")
            return

        order_id = f"R{len(orders) + 1:04d}"
        orders.append(
            {
                "id": order_id,
                "customer_id": cid,
                "device_id": device_info.split(":")[0],
                "issue": issue,
                "technician": tech_entry.get().strip(),
                "status": status_combo.get(),
                "service_cost": service_cost,
                "parts_cost": parts_cost,
                "tax_rate": 0.10,
                "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

        messagebox.showinfo("Success", f"Repair order {order_id} created successfully!")

        issue_text.delete("1.0", tk.END)
        service_entry.delete(0, tk.END)
        service_entry.insert(0, "0")
        parts_entry.delete(0, tk.END)
        parts_entry.insert(0, "0")

        refresh_orders()

    ttk.Button(form, text="Create Order", command=save_order).grid(
        row=7, column=0, columnspan=2, pady=10
    )

    refresh_orders()
    return frame


# ---------------- Billing Tab ----------------

def create_billing_tab(parent):
    frame = ttk.Frame(parent)

    select_frame = ttk.LabelFrame(frame, text="Select Order", padding="10")
    select_frame.pack(side="top", fill="x", padx=5, pady=5)

    ttk.Label(select_frame, text="Order ID:").pack(side="left", padx=5)
    order_combo = ttk.Combobox(select_frame, width=20)
    order_combo["values"] = [o["id"] for o in orders]
    order_combo.pack(side="left", padx=5)

    invoice_frame = ttk.LabelFrame(frame, text="Invoice", padding="10")
    invoice_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

    invoice_text = scrolledtext.ScrolledText(invoice_frame, width=70, height=20)
    invoice_text.pack(fill="both", expand=True)

    def generate_invoice():
        oid = order_combo.get()
        if not oid:
            messagebox.showerror("Error", "Please select an order")
            return

        order = None
        for o in orders:
            if o["id"] == oid:
                order = o
                break
        if not order:
            messagebox.showerror("Error", "Order not found")
            return

        customer = None
        for c in customers:
            if c["id"] == order["customer_id"]:
                customer = c
                break
        if not customer:
            messagebox.showerror("Error", "Customer not found")
            return

        device = None
        for d in customer["devices"]:
            if d["id"] == order["device_id"]:
                device = d
                break

        subtotal, tax, total = calculate_total(
            order["service_cost"], order["parts_cost"], order["tax_rate"]
        )

        invoice = f"""
{'='*60}
                    REPAIRMATE INVOICE
{'='*60}

Order ID: {order['id']}
Date: {order['date_created']}

CUSTOMER INFORMATION:
Name: {customer['name']}
Email: {customer['email']}
Phone: {customer['phone']}
Address: {customer['address']}

DEVICE INFORMATION:
Model: {device['model'] if device else 'N/A'}
Brand: {device['brand'] if device else 'N/A'}
Type: {device['type'] if device else 'N/A'}

REPAIR DETAILS:
Issue: {order['issue']}
Technician: {order['technician']}
Status: {order['status']}

{'='*60}
BILLING DETAILS:
{'='*60}
Service Cost:                             ${order['service_cost']:,.2f}
Parts Cost:                               ${order['parts_cost']:,.2f}
                                          ----------
Subtotal:                                 ${subtotal:,.2f}
Tax ({order['tax_rate']*100}%):                                  ${tax:,.2f}
                                          ----------
TOTAL:                                    ${total:,.2f}
{'='*60}

Thank you for choosing RepairMate!
"""
        invoice_text.delete("1.0", tk.END)
        invoice_text.insert("1.0", invoice)

    ttk.Button(select_frame, text="Generate Invoice", command=generate_invoice).pack(
        side="left", padx=5
    )

    return frame


def create_reports_tab(parent):
    frame = ttk.Frame(parent)

    search_frame = ttk.LabelFrame(frame, text="Search & Filter", padding="10")
    search_frame.pack(side="top", fill="x", padx=5, pady=5)

    ttk.Label(search_frame, text="Search Type:").grid(
        row=0, column=0, sticky="e", padx=5, pady=5
    )
    search_type = ttk.Combobox(
        search_frame,
        width=20,
        values=["Device Model", "Status", "Customer Name", "Order ID"],
    )
    search_type.set("Status")
    search_type.grid(row=0, column=1, pady=5, padx=5)

    ttk.Label(search_frame, text="Search Text:").grid(
        row=0, column=2, sticky="e", padx=5, pady=5
    )
    search_entry = ttk.Entry(search_frame, width=25)
    search_entry.grid(row=0, column=3, pady=5, padx=5)

    results_frame = ttk.LabelFrame(frame, text="Search Results", padding="10")
    results_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

    columns = ("Order ID", "Customer", "Device", "Status", "Technician", "Total Cost")
    tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    def show_all():
        tree.delete(*tree.get_children())
        for o in orders:
            customer = None
            for c in customers:
                if c["id"] == o["customer_id"]:
                    customer = c
                    break
            device = None
            if customer:
                for d in customer["devices"]:
                    if d["id"] == o["device_id"]:
                        device = d
                        break
            subtotal, tax, total = calculate_total(
                o["service_cost"], o["parts_cost"], o["tax_rate"]
            )
            tree.insert(
                "",
                "end",
                values=(
                    o["id"],
                    customer["name"] if customer else "N/A",
                    (device["brand"] + " " + device["model"]) if device else "N/A",
                    o["status"],
                    o["technician"],
                    f"${total:,.2f}",
                ),
            )

    def perform_search():
        text = search_entry.get().strip().lower()
        if not text:
            messagebox.showerror("Error", "Enter search text")
            return

        tree.delete(*tree.get_children())
        field = search_type.get()

        for o in orders:
            customer = None
            for c in customers:
                if c["id"] == o["customer_id"]:
                    customer = c
                    break
            device = None
            if customer:
                for d in customer["devices"]:
                    if d["id"] == o["device_id"]:
                        device = d
                        break

            match = False
            if field == "Status" and text in o["status"].lower():
                match = True
            elif field == "Order ID" and text in o["id"].lower():
                match = True
            elif field == "Customer Name" and customer and text in customer["name"].lower():
                match = True
            elif field == "Device Model" and device and text in device["model"].lower():
                match = True

            if match:
                subtotal, tax, total = calculate_total(
                    o["service_cost"], o["parts_cost"], o["tax_rate"]
                )
                tree.insert(
                    "",
                    "end",
                    values=(
                        o["id"],
                        customer["name"] if customer else "N/A",
                        (device["brand"] + " " + device["model"])
                        if device
                        else "N/A",
                        o["status"],
                        o["technician"],
                        f"${total:,.2f}",
                    ),
                )

        messagebox.showinfo("Search Complete", "Search finished")

    ttk.Button(search_frame, text="Search", command=perform_search).grid(
        row=0, column=4, padx=5
    )
    ttk.Button(search_frame, text="Show All", command=show_all).grid(
        row=0, column=5, padx=5
    )

    stats_frame = ttk.LabelFrame(frame, text="Statistics", padding="10")
    stats_frame.pack(side="bottom", fill="x", padx=5, pady=5)

    stats_label = ttk.Label(stats_frame, text="", font=("Arial", 10))
    stats_label.pack()

    def update_stats():
        total_customers = len(customers)
        total_orders = len(orders)
        pending = len([o for o in orders if o["status"] == "Pending"])
        completed = len([o for o in orders if o["status"] == "Completed"])
        stats_label.config(
            text=f"Total Customers: {total_customers}  |  Total Orders: {total_orders}  |  Pending: {pending}  |  Completed: {completed}"
        )

    ttk.Button(stats_frame, text="Refresh Statistics", command=update_stats).pack(
        pady=5
    )

    show_all()
    update_stats()

    return frame


def calculate_total(service_cost, parts_cost, tax_rate=0.10):
    try:
        subtotal = float(service_cost) + float(parts_cost)
        tax = subtotal * tax_rate
        total = subtotal + tax
        return subtotal, tax, total
    except Exception:
        messagebox.showerror("Error", "Invalid cost values for calculation")
        return 0, 0, 0




def main():
    root = tk.Tk()
    show_login(root)
    root.mainloop()



main()


