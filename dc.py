import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 13
GPIO.setup(pwmPin, GPIO.OUT)

pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

dcmin = 0 
dcmax = 100

try:
  while True:
    for dc in range(dcmax,dcmin, -1):
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.02)
except KeyboardInterrupt:
  print("closing")

GPIO.cleanup()