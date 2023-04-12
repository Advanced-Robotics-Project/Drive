import keyboard, requests

class KeyboardControl:
    def __init__(self):
        self.verbose = True

        self.deepracer_name = "odroid"
        self.deepracer_password = "deepracer1234"
        self.deepracer_ip = "odroid.local"
        self.port = ":1234"

        self.last_command = ""

        keyboard.hook(self.dump)
        keyboard.wait("esc")
        keyboard.unhook_all()
        self.stop()
        exit()

    def forward(self):
        requests.get("http://"+self.deepracer_ip+self.port+"/forward")

    def left(self):
        requests.get("http://"+self.deepracer_ip+self.port+"/left")

    def backward(self):
        requests.get("http://"+self.deepracer_ip+self.port+"/backward")

    def right(self):
        requests.get("http://"+self.deepracer_ip+self.port+"/right")

    def reset_throttle(self):
        requests.get("http://"+self.deepracer_ip+self.port+"/reset_throttle")

    def reset_angle(self):
        requests.get("http://"+self.deepracer_ip+self.port+"/reset_angle")

    def stop(self):
        requests.get("http://"+self.deepracer_ip+self.port+"/stop")

    def dump(self, x):
        f = keyboard.KeyboardEvent('down',72,'up')
        d = keyboard.KeyboardEvent('down',80,'down')
        l = keyboard.KeyboardEvent('down',75,'left')
        r = keyboard.KeyboardEvent('down',77,'right')
        if x.event_type == 'down' and x.name==f.name:
            self.forward()
        elif x.event_type == 'down' and x.name==d.name:
            self.backward()
        elif x.event_type == 'down' and x.name==l.name:
            self.left()
        elif x.event_type == 'down' and x.name==r.name:
            self.right()
        elif x.event_type == 'up' and x.name==f.name:
            self.reset_throttle()
        elif x.event_type == 'up' and x.name==d.name:
            self.reset_throttle()
        elif x.event_type == 'up' and x.name==l.name:
            self.reset_angle()
        elif x.event_type == 'up' and x.name==r.name:
            self.reset_angle()

if __name__=="__main__":
    kc = KeyboardControl()

