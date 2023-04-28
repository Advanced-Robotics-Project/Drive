import time, keybaord
from http.server import HTTPServer, BaseHTTPRequestHandler

from Pololu import Pololu

max_throttle = 1400 # forward
zero_throttle = 1450 # stop
min_throttle = 1500 # backward

max_left = 1000 # left
max_right = 2000 # right
zero_angle = 1500 # neutral

angle = zero_angle
throttle = zero_throttle

p = Pololu()

class ControlServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global throttle, angle
        if self.path == "/" or self.path == "/stop":
            angle = zero_angle
            throttle = zero_throttle
        elif self.path == "/forward":
            throttle = max_throttle
        elif self.path == "/backward":
            throttle = min_throttle
        elif self.path == "/left":
            angle = max_left
        elif self.path == "/right":
            angle = max_right
        elif self.path == "/reset_angle":
            angle = zero_angle
        elif self.path == "/reset_throttle":
            throttle = zero_throttle
        elif self.path == "/quit":
            print("shutting down server")
            self.server.socket.close()
            sys.exit()
        print(angle,throttle)
        p.set_pwm(angle,1)
        p.set_pwm(throttle,0)
        self.send_response(200)

if __name__=="__main__":
    port = 1234
    server = HTTPServer(("192.168.50.136",port), ControlServer)
    print("server started at port "+str(port))
    server.serve_forever()
