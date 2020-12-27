from time import sleep, sleep_ms
from gc import collect, mem_free
from devices import SENSOR
from ui import UserInterface
from machine import RTC
from utime import localtime
from themes import *
rtc = RTC()
print("Synchronize time from NTP server ...")
rtc.ntp_sync(server="0.ua.pool.ntp.org", tz="Europe/Kiev")
while not rtc.synced():
    sleep_ms(100)
    break

collect()

theme = mini
ui = UserInterface(theme)
sensor = SENSOR()

while KeyboardInterrupt:
    _raw_time = localtime()
    _date = str(_raw_time[2]) + '/' + str(_raw_time[1]) + '/' + str(_raw_time[0])
    _time = "{:0>2}".format(_raw_time[3] + 2) + ":{:0>2}".format(_raw_time[4])
    ui.mem_free_label(mem_free())
    ui.temp_label(sensor.temperature)
    ui.humi_label(sensor.humidity)
    ui.pres_label(sensor.pressure)
    ui.time_label(_time)
    collect()
    sleep(0.5)
