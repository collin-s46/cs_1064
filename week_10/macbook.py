#attribute 1: battery
#attribute 2: powered on
class Macbook:
    def __init__(self, battery, is_on):
        self.battery = battery
        self.is_on = is_on

    def power_on(self):
        self.is_on = True
        print('Powered on!')

class MacbookAir(Macbook):
    def __init__(self, battery, is_on, screen_size):
        super().__init__(battery, is_on)
        self.screen_size = screen_size

    def display(self):
        print(f'Screen size: {self.screen_size} inches' )


my_mac = MacbookAir(85, False, 15)

my_mac.power_on()

my_mac.display()