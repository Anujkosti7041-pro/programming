class Device:
    def __init__(self, model, issue, status="Pending"):
        self.model = model
        self.issue = issue
        self.status = status


class Customer:
    def __init__(self, cid, name, phone):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
