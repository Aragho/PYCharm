class Bike():
    def __init__(self):
        self.is_on = False
        self.gear = 0
        self.acceleration = 0
        self.deceleration = 0

    def turn_on(self):
        self.is_on = True
        return self.is_on

    def turn_off(self):
        self.is_on = False
        return self.is_on

    def accelerate(self, speed, gear):
        is_on = True
        if (speed > 0 and speed <= 20):
            gear == 1
            self.acceleration = speed + gear
        elif (speed > 20 and speed <= 30):
            gear == 2
            self.acceleration = speed + gear

        elif (speed > 30 and speed <= 40):
            gear = 3
            self.acceleration = speed + gear
        elif (speed > 40):
            gear == 4
            self.acceleration = speed + gear

        else:
            is_on = False

    def get_accelerate(self):
        return self.acceleration

    def deccelerate(self, speed, gear):
        is_on = True
        if (speed > 0 and speed <= 20):
            gear == 1
            self.deceleration = speed - gear

        elif (speed > 20 and speed <= 30):
            gear == 2
            self.deceleration = speed - gear

        elif (speed > 30 and speed <= 40):
            gear == 3
            self.deceleration = speed - gear

        elif (speed > 40):
            gear == 4
            self.deceleration = speed - gear

    def get_accelerate(self):
        return self.acceleration

    def get_decelerate(self):
        return self.deceleration
