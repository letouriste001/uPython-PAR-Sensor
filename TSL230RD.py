import pyb

timer = 0
t2 = None
period = 1


# TODO commentaire
def callback(line):
    global timer
    global t2
    global period
    tmp = t2.counter()
    period = tmp - timer
    timer = tmp


# TODO foonction e de moyenne pour ameliorer la valeur lue
def measure():
    global period
    try:
        return 1000000 / period
    except ZeroDivisionError:
        return -1


def init(pin_name='X1'):
    global t2
    pin = pyb.Pin(pin_name, pyb.Pin.IN)
    pyb.Pin(pin)
    t2 = pyb.Timer(2, prescaler=83, period=0x0fffffff)
    pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_UP, callback)
