class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"  # !r call __repr__ method of self.name
    
    def disconnected(self):
        self.connected = False
        print("Disconnected")

class Printer(Device): # Inherit Device class
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by) # This super() calls the __init__() method from super or parent class
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("your printer is not connected")
            return
        print(f"printing {pages} pages.")
        self.remaining_pages -= pages
        
# printer = Device("printer", "USB")
# print(printer)
# printer.disconnected()     

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnected()
printer.print(30)