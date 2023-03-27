import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pinSwitchUp = 13 #in
GPIO.setup(pinSwitchUp, GPIO.IN)

pinSwitchDown = 16 #in
GPIO.setup(pinSwitchDown, GPIO.IN)

fill=0

def countUp(channel):
    global fill
    fill = fill + 10
    if fill >= 100:
        fill = 100
    p.ChangeDutyCycle(fill)
    print(f"f = {f} Hz, fill = {fill} %")

def countDown(channel):
    global fill
    fill = fill - 10
    if fill <= 0:
        fill = 0
    p.ChangeDutyCycle(fill)
    print(f"f = {f} Hz, fill = {fill} %")
    
pin = 27
GPIO.setup(pin, GPIO.OUT)
f = 50 #50 Hz
fill = 0 # fill 90%
#pwm üzemmód bekapcsolása
p = GPIO.PWM(pin, f)
#indítás
p.start(fill)
print(f"f = {f} Hz, fill = {fill} %")
   
                
    
# Esemény összekapcsolása az eseménykezelővel
GPIO.add_event_detect(pinSwitchUp, GPIO.FALLING, callback=countUp, bouncetime=200)
GPIO.add_event_detect(pinSwitchDown, GPIO.FALLING, callback=countDown, bouncetime=200)


try:
    while True:
        # Led fel, le
        time.sleep(0.3)
                
                
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
    