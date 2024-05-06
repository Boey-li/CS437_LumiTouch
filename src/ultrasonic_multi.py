#Start by importing all necessary libraries and packages 
import RPi.GPIO as GPIO
import time

#Set the GPIO to BCM Mode
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN) 

#Set Pin 4 to be our Sniffer Pin, We want this to be an Input so we set it as such
GPIO.setup(4,GPIO.IN)

#Set GPIO pins for the LEDs
LED_PIN1 = 17
LED_PIN2 = 27
LED_PIN3 = 22
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)


def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("distance: ", distance)
    return distance

#This variable will be used to determine if pressure is being applied or not
prev_input = 0

#Create a Loop that goes on as long as the script is running
try:
    while True:

        #take a reading from the pressure pad (based on the voltage able to get to pin 4)
        pressure = GPIO.input(4)
        distance = get_distance()
        #if the last reading was low and this one high the pressure pad is being pressed!
        if pressure == 1 and distance < 20:
        #Print that fact to the shell, RIP David Bowie
            GPIO.output(LED_PIN1, GPIO.HIGH)
            GPIO.output(LED_PIN2, GPIO.HIGH)
            GPIO.output(LED_PIN3, GPIO.HIGH)
            print("LED ON: All LEDs are lit")
        elif pressure == 1 and distance < 40:
            GPIO.output(LED_PIN1, GPIO.HIGH)
            GPIO.output(LED_PIN2, GPIO.HIGH)
            GPIO.output(LED_PIN3, GPIO.LOW)
            print("LED ON: Two LEDs are lit")
        elif pressure == 1 and distance < 60:
            GPIO.output(LED_PIN1, GPIO.HIGH)
            GPIO.output(LED_PIN2, GPIO.LOW)
            GPIO.output(LED_PIN3, GPIO.LOW)
            print("LED ON: One LEDs are lit")
            
        else:
            GPIO.output(LED_PIN1, GPIO.LOW)
            GPIO.output(LED_PIN2, GPIO.LOW)
            GPIO.output(LED_PIN3, GPIO.LOW)

        #update previous input so we can avoid spamming the Shell with messages, 
        #this section of the script is also a perfect place to add threshold values to active other devices 
        #Have a slight pause here, also to avoid  spamming the shell with data
        time.sleep(0.10)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    


