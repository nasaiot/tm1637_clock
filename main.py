import tm1637
from machine import Pin,RTC
import network, usocket, utime, ntptime
from time import sleep
print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('wifi', 'passwd')
while not wifi.isconnected():
    pass
print("Connected")

tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))
tm.brightness(1)
ntptime.settime()

while(True):
    sleep(60)
    local_time_sec = utime.time() + 8 * 3600
    local_time = utime.localtime(local_time_sec)
    h=local_time[3]
    m=local_time[4]
    print(local_time)
    tm.numbers(h, m)
