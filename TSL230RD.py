import pyb

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
def raw_measure():
    global period
    try:
        return 1000000 / period
    except ZeroDivisionError:
        return -1


# TODO fonction a verifier exactement
def watt_m2_measure():
    f0 = raw_measure()
    return ((f0 * 100) - 0.4) / 790


def init(pin_name='X1', frequency_scalling=100):
    global t2
    global f0_scalling
    f0_scalling = frequency_scalling
    pin = pyb.Pin(pin_name, pyb.Pin.IN)
    pyb.Pin(pin)
    t2 = pyb.Timer(2, prescaler=83, period=0x0fffffff)
    pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_UP, callback)
