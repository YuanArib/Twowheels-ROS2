import Jetson.GPIO as GPIO
from pca9685_driver import Device
from time import sleep
import sys
from sshkeyboard import listen_keyboard

def set_duty_cycle(pwmdev, channel, dt):
    """
    @pwmdev a Device class object already configured
    @channel Channel or PIN number in PCA9685 to configure 0-15
    @dt desired duty cycle
    """
    val = (dt*4095)//100
    pwmdev.set_pwm(channel,val)

def forward(pwmdev):
    pwmdev.set_pwm(15, 2000)
    pwmdev.set_pwm(5, 2000)
    pwmdev.set_pwm(14, 0)
    pwmdev.set_pwm(4, 0)

def backward(pwmdev):
    pwmdev.set_pwm(14, 2000)
    pwmdev.set_pwm(4, 2000)
    pwmdev.set_pwm(15, 0)
    pwmdev.set_pwm(5, 0)

def right(pwmdev):
    pwmdev.set_pwm(14, 2000)
    pwmdev.set_pwm(5, 2000)
    pwmdev.set_pwm(15, 0)
    pwmdev.set_pwm(4, 0)

def left(pwmdev):
    pwmdev.set_pwm(15, 2000)
    pwmdev.set_pwm(4, 2000)
    pwmdev.set_pwm(14, 0)
    pwmdev.set_pwm(5, 0)

def stop(pwmdev):
    pwmdev.set_pwm(15, 0)
    pwmdev.set_pwm(14, 0)
    pwmdev.set_pwm(4, 0)
    pwmdev.set_pwm(5, 0)

GPIO.setmode(GPIO.BOARD)

pca9685 = Device(0x40, 7)

pca9685.set_pwm_frequency(1000)

# set_duty_cycle(pca9685,12,5)

print("Enter Key to change direction / quit... (up/Forward, down/Backward, right/Right, left/Left, q/Quit)")
def press(key):
      if key == "right":
        right(pca9685)
        print("Currently Going Right")
      elif key == "left":
        left(pca9685)
        print("Currently Going Left")
      elif key == "up":
        forward(pca9685)
        print("Currently Going Forward")
      elif key == "down":
        backward(pca9685)
        print("Currently Going Backward")
      elif key == "q":
        stop(pca9685)
        print("Quitting")

def release(key):
  stop(pca9685)

listen_keyboard(
    on_press=press,
    on_release=release,
)