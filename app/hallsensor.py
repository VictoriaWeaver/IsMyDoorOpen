# import modules
import RPi.GPIO as GPIO
import time
import datetime


def gpio_setup():
    '''
        Setup the GPIO pins for the Hall Sensor
    '''
    GPIO.setmode(GPIO.BCM)  # set up BCM GPIO numbering
    GPIO.setup(25, GPIO.IN)  # set GPIO 25 as the input from the Hall Effect Sensor


def sensor_callback():
    '''
        Prints the status of the "door" opening or closing and the time at which the even occurs
    '''
    today = datetime.date.today()
    timestamp = time.time()
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

    # NOTE: might have to reverse behavior based upon Hall Sensor (active low or active high)
    if GPIO.input(25):
        # Rising edge
        print "Door is open on {} at {}".format(today, timestamp)
    else:
        # Falling edge
        print "Door is closed on {} at {}".format(today, timestamp)


def main():
    '''
        Temporary test to detect interrupts over the period of one minute.
        For every edge detected on the GPIO (both rising and falling), the state of the "door" will be printed
    '''
    gpio_setup()
    GPIO.add_event_detect(25, GPIO.BOTH, callback=sensor_callback)
    # run for one minute (temporary)
    time.sleep(60)
    GPIO.cleanup()  # reset all the GPIO pins to input values for safety
