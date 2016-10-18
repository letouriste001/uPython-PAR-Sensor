"""TSL230RD.py: Capteur de par pour pybboard."""

__author__ = "Christophe AUBERT"
__copyright__ = "Copyright 2016"
__credits__ = ["Christophe AUBERT"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Christophe AUBERT"
__status__ = "Production"

import pyb

# Constantes
FACOTR_A = 0.34
FACOTR_B = -30.6

# variables globales
timer = 0
t2 = None
period = 1
f0_scalling = None


# TODO commentaire
def callback(line):
    global timer
    global t2
    global period
    tmp = t2.counter()
    period = tmp - timer
    timer = tmp


# TODO fonction de moyenne pour ameliorer la valeur lue
def raw_average(time_average=10):
    for i in range(0, (time_average - 1)):
        sum += raw_measure()
        pyb.delay(1000)
    try:
        return sum / time_average
    except ZeroDivisionError:
        print("division by zero, time average is bad, please change value")
        return -1


#TODO commentaire
def raw_measure():
    global period
    try:
        return 1000000 / period
    except ZeroDivisionError:
        print("division by zero, period is null, please check your wiring")
        return -1


# TODO fonction a verifier exactement
def uwatt_by_cm2_measure():
    f0 = raw_measure()
    return ((f0 * 100) - 0.4) / 790


# TODO fonction a verifier exactement
def uwatt_by_cm2_average_measure(time_average=10):
    f0 = raw_average(time_average)
    return ((f0 * 100) - 0.4) / 790


# TODO ameliorer la fonction et la commenter
def Einstein_by_m2_by_second_measure():
    f0 = raw_measure()
    return ((f0 * FACOTR_A) + FACOTR_B)


# TODO ameliorer la fonction et la commenter
def Einstein_by_m2_by_second_average_measure(time_average=10):
    f0 = raw_average(time_average)
    return ((f0 * FACOTR_A) + FACOTR_B)


#TODO Commenter
def init(pin_name='X1', frequency_scalling=100):
    global t2
    global f0_scalling
    f0_scalling = frequency_scalling
    pin = pyb.Pin(pin_name, pyb.Pin.IN)
    pyb.Pin(pin)
    t2 = pyb.Timer(2, prescaler=83, period=0x0fffffff)
    pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_UP, callback)
