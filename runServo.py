from pololu import Pololu
import time

p = Pololu()

p.set_pwm(1200,1)
time.sleep(5)
p.set_pwm(1500,1)
