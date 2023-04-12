import serial
import serial.tools.list_ports as stl

class Pololu:
    def __init__(self):
        pid = 139
        vid = 8187
        port = None
        for p in stl.comports():
            if p.pid == pid and p.vid == vid: port = p
        self.pololu = serial.Serial("/dev/" + port.name)

    def set_pwm(self, pwm:int, channel:int):
        pwm_quarter = pwm*4
        lower7 = pwm_quarter & 0b1111111
        upper7 = (pwm_quarter>>7) & (0b1111111)
        print(lower7)
        print(upper7)
        ba = bytearray([0x84, channel, lower7, upper7])
        self.pololu.write(ba)
