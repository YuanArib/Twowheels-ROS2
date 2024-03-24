import Jetson.GPIO as GPIO
# from pca9685_driver import Device

GPIO.setmode(GPIO.BOARD)

class Motor:
    alpha = 1.0 
    beta = 0.0

    def __init__(self, driver, channel1, channel2, *args, **kwargs) -> None:
        self._driver = driver
        self._ina = channel1
        self._inb = channel2
        self._value = 0

    def _write_value(self, value):
        mapped_value = int(255.0 * (self.alpha * value + self.beta))
        speed = min(max(abs(mapped_value), 0), 255)
        if mapped_value < 0:
            #FORWARD
            self._driver.set_pwm(self._ina, 0)
            self._driver.set_pwm(self._inb, speed * 16)
        else:
            #BACKWARD
            self._driver.set_pwm(self._ina, speed * 16)
            self._driver.set_pwm(self._inb, 0)   

    def _release(self):
        self._driver.set_pwm(self._ina, 0)
        self._driver.set_pwm(self._inb, 0) 
    
    def set_speed(self, speed):
        self._write_value(speed)