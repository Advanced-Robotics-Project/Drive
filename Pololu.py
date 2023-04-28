import time, serial
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

    def get_voltage(self, channel:int):
        self.pololu.write(bytearray([0x90, channel]))
        time.sleep(0.1)
        b = self.pololu.read_all()
        if len(b)==0: return -1
        lower, upper = b[0], b[1]
        signal = (upper<<8)+lower
        return signal/1023*5 # 0-1023 mapped to 0-5 V
