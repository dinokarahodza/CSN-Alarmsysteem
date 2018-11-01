import RPi.GPIO as GPIO #Import the GPIO library
import time #Used for waiting between beeps

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Set buzzer - pin 18 as output
buzzer = 22
x = False
GPIO.setup(buzzer, GPIO.OUT)
for i in range(500):
    input_state = GPIO.input(17)

    if not input_state:
        x = not x
        if x:
            GPIO.output(buzzer, GPIO.HIGH)
            print("Beep")
            time.sleep(0.5)  # Delay in seconds
        else:
            GPIO.output(buzzer, GPIO.LOW)
            print("No Beep")
            time.sleep(0.5)
        print('Button pressed')
        time.sleep(0.1)
    else:
        print('Button not pressed')
        time.sleep(0.1)
GPIO.cleanup()