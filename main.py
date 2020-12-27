from time import sleep, sleep_ms
from gc import collect, mem_free
from devices import SENSOR
from ui import UserInterface
from rgb565color import *
from machine import RTC
from utime import localtime
rtc = RTC()
print("Synchronize time from NTP server ...")
rtc.ntp_sync(server="0.ua.pool.ntp.org", tz="Europe/Kiev")
while not rtc.synced():
    sleep_ms(100)
    break
print(localtime())
collect()

ui = UserInterface()
sensor = SENSOR()

while KeyboardInterrupt:
    _raw_time = localtime()
    _date = str(_raw_time[2]) + '/' + str(_raw_time[1]) + '/' + str(_raw_time[0])
    _time = "{:0>2}".format(_raw_time[3] + 2) + ":{:0>2}".format(_raw_time[4])
    ui.mem_free_label(mem_free(), 0xFDE58B)
    ui.temp_label(sensor.temperature, 0x000000)
    ui.humi_label(sensor.humidity, 0x000000)
    ui.pres_label(sensor.pressure, 0xFDC168)
    ui.time_label(_time, 0xFDE58B)
    collect()
    sleep(0.5)
