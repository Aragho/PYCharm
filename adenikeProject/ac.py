class Ac():
    def __init__(self):
        self.is_on = False
        self.temperature = 16

    def turn_on(self):
        self.is_on = True
        return self.is_on

    def turn_off(self):
        self.is_on = False
        return self.is_on


    def get_temperature(self):
        return self.temperature

    def increased(self):
        if self.turn_on:
            self.temperature +=1

    def decreased(self):
        if self.turn_on:
            if self.temperature >= 16:
                self.temperature -=1
            else:
                self.temperature = 16








