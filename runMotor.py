from pololu import Pololu
import time

p = Pololu()
p.set_pwm(1100,1)
p.set_pwm(1450,0)
time.sleep(5)
p.set_pwm(1400,0)
time.sleep(5)
p.set_pwm(1450,0)
