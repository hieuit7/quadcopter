import pigpio
class QuadCenter:
    def __init__(self):

        self.dc1 = 12
        self.dc2 = 18
        self.dc3 = 13
        self.dc4 = 19
        self.pi = pigpio.pi()
        self.pi.set_servo_pulsewidth(self.dc1,0)
        self.pi.set_servo_pulsewidth(self.dc2, 0)
        self.pi.set_servo_pulsewidth(self.dc3, 0)
        self.pi.set_servo_pulsewidth(self.dc4, 0)

    def increase(self, pin, speed):
        self.pi.set_servo_pulsewidth(pin, speed)

    def start(self, speed):
        self.pi.set_servo_pulsewidth(self.dc1, speed)
        self.pi.set_servo_pulsewidth(self.dc2, speed)
        self.pi.set_servo_pulsewidth(self.dc3, speed)
        self.pi.set_servo_pulsewidth(self.dc4, speed)
