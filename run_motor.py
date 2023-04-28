from Pololu import Pololu
import time

p = Pololu()
p.set_pwm(1100,1) # channel 1 steer
p.set_pwm(1450,0) # channel 0 stop throttle
time.sleep(5)
p.set_pwm(1400,0) # channel 0 forward throttle
time.sleep(5)
p.set_pwm(1450,0) # channel 0 stop throttle
