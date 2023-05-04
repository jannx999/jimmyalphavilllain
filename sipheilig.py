import RPi.GPIO as GPIO
import time
# Pin-Definitionen
motor1_pin1 = 31 # Input 1 des Motors 1
motor1_pin2 = 33 # Input 2 des Motors 1
motor2_pin1 = 35 # Input 1 des Motors 2
motor2_pin2 = 37 # Input 2 des Motors 2

# Initialisierung der GPIO-Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

try:                                           #Motoren drehen sich 
    while True:
        GPIO.output(motor1_pin1, GPIO.HIGH)
        GPIO.output(motor1_pin2, GPIO.LOW)
        GPIO.output(motor2_pin1, GPIO.HIGH)
        GPIO.output(motor2_pin2, GPIO.LOW)
            
except KeyboardInterrupt:      #keyboard stopp kein Motor dreht 
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)
    # Aufräumen
    GPIO.cleanup()
