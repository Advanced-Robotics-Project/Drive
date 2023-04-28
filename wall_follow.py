import time

from Drive import Drive

drive = Drive()

def main():
    # drive.motor(1) # full throttle forward
    while True:
        d = drive.distance()
        print("distance [cm]:",d)
        if d==-1:
            drive.steer(1) # steer right
        elif d>80:
            drive.steer(-1) # steer left
        else:
            drive.steer(0)
        time.sleep(0.2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        drive.stop()
        drive.steer_neutral()
