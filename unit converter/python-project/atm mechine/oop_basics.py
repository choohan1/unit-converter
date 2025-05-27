class atm:
    totall_balance = 1000

    def __init__(self, name: str, pin: str):
        self.name = name
        self.pin = pin

    def check_pin(self, pin: str):
        if self.pin == pin:
            print("correct pin")
        else:
            print("incorrect pin")
