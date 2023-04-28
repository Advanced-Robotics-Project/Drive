import time
from Drive import Drive

d = Drive()
while True:
    print("Distance [cm]:",d.distance())
    time.sleep(0.5)
