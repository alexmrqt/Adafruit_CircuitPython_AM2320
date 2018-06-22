import time
from machine import I2C
import adafruit_am2320

i2c = I2C(0, I2C.MASTER)
i2c.init(I2C.MASTER, baudrate=100000)
am = adafruit_am2320.AM2320(i2c)


while True:
    try:
        print("Temperature: ", am.temperature)
        print("Humidity: ", am.relative_humidity)
    except OSError:
        # These sensors are a bit flakey, its ok if the readings fail
        pass
    except RuntimeError:
        pass
    time.sleep(2)
