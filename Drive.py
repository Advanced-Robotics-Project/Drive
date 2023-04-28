from Pololu import Pololu

class Drive:
    def __init__(self):
        self.pololu = Pololu()

        self.channel_motor = 0
        self.channel_steer = 1
        self.channel_ir = 11

        self.max_throttle = -50 # max forward
        self.pwm_zero_motor = 1450 # stop

        self.max_left = 500 # steer left
        self.pwm_zero_steer = 1500 # steer neutral

    # v: float in range [-1,1]
    # v = 1: full throttle forward
    # v = -1: full throttle backwawrd
    def motor(self, v:float):
        if v<-1.0 or v>1.0: return
        self.pololu.set_pwm(
            self.pwm_zero_motor + int(self.max_throttle*v),
            self.channel_motor
        )

    # v: float in range [-1,1]
    # v = 1: steer fully right
    # v = -1: steer fully left
    def steer(self, v:float):
        if v<-1.0 or v>1.0: return
        self.pololu.set_pwm(
            self.pwm_zero_steer + int(self.max_left*v),
            self.channel_steer
        )

    def stop(self):
        self.pololu.set_pwm(
            self.pwm_zero_motor,
            self.channel_motor
        )

    def distance(self): # returns voltage in cm
        v = self.pololu.get_voltage(self.channel_ir)
        d = 1/((v*1000-1125)/137500)
        if d<70 or v<1.4 or v>3.3: return -1.0 # out of range, invalid data
        return d
