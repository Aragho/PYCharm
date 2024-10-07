class Tv:

    def __init__(self):
        self.setOn = False
        self.channel = 0
        self.volume = 0

    def turn_on(self):
        self.setOn = True
        return self.setOn

    def turn_Off(self):
        self.setOn = False
        return self.setOn

    def get_Channel(self):
        if self.setOn:
            return self.channel

    def set_Channel(self, number):
        if self.setOn:
            self.channel = number
            return self.channel

    def get_volume(self):
        if self.setOn:
            return self.volume

    def set_volume(self, number):
        if self.setOn:
            self.volume = number
            return self.volume

    def channel_up(self):
        if self.setOn:
            self.channel += 1



    def channel_down(self):
        if self.setOn == True:
            self.channel -= 1

    def volume_up(self):
        if self.setOn == True:
            self.volume += 1

    def volume_down(self):
        if self.setOn == True:
            self.volume -= 1











