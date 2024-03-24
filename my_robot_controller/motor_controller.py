import Jetson.GPIO as GPIO
from pca9685_driver import Device
from my_robot_controller.motor import Motor

GPIO.setmode(GPIO.BOARD)

class MotorController:
    address = 0x40
    bus_number = 7
    # modify below code according to the pins in the pca9685
    LF_1 = 0
    LF_2 = 0
    RF_1 = 0
    RF_2 = 0
    LR_1 = 0
    LR_2 = 0
    RR_1 = 0
    RR_2 = 0

    def __init__(self):
        self._motor_driver = Device(0x40, 7)
        self._left_front_motor = Motor(
            driver = self._motor_driver,
            channel1 = self.LF_1,
            channel2 = self.LF_2
        )
        self._right_front_motor = Motor(
            driver = self._motor_driver,
            channel1 = self.RF_1,
            channel2 = self.RF_2
        )
        self._left_rear_motor = Motor(
            driver = self._motor_driver,
            channel1 = self.LR_1,
            channel2 = self.LR_2
        )
        self._right_rear_motor = Motor(
            driver = self._motor_driver,
            channel1 = self.RR_1,
            channel2 = self.RR_2
        )

    def set_motors(self, left_speed, right_speed):
            print(f"Set AdaFruit motors to {left_speed}, {right_speed}")
            self._left_front_motor.set_speed(left_speed)
            self._left_rear_motor.set_speed(left_speed)
            self._right_front_motor.set_speed(right_speed)
            self._right_rear_motor.set_speed(right_speed)