# Write your code here :-)
import time
import board
from analogio import AnalogIn
from analogio import AnalogOut
import adafruit_ssd1306

# requires: adafruit_ssd1306
#           adafruit_bus_device
#           adafruit_framebuf
#           font5x8.bin (place in root)

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(width=128, height=64, i2c=i2c)
analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)
start_time = time.monotonic()

while True:
    newtime = time.monotonic() - start_time
    if newtime <= 60:
        disptime = "Time: {:.2f} Seconds".format(newtime)
    if newtime > 60:
        disptime = "Time: {:.2f} Minutes".format(newtime / 60)
    if newtime > 3600:
        disptime = "Time: {:.2f} Hours".format(newtime / 3600)

    # start at 30000 to compenstate for LED Vf
    for i in range(30000, 65535, 1024):
        analog_out.value = i
        oled.fill(0)
        oled.text("IMSAI Guy", 0, 0, 1)
        oled.text(disptime, 0, 12, 1)
        volt_string = "Volts: {:.2f}".format(3.3 * analog_in.value / 65535)
        oled.text(volt_string, 0, 24, 1)
        oled.show()
