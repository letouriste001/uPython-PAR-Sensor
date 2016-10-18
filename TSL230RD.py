"""TSL230RD.py: Capteur de par pour pybboard."""

__author__ = "Christophe AUBERT"
__copyright__ = "Copyright 2016"
__credits__ = ["Christophe AUBERT"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Christophe AUBERT"
__status__ = "development"

import pyb

# Constantes
FACOTR_A = 0.34
FACOTR_B = -30.6

# Cf datasheet TSL230 RD
DARK_FREQUENCY = 0.4
RESPONSIVITY = 790

# Cf micro python reference
# variable compteur de microsecondes
TIMER = 2
PRESCALER = 83
PERIOD = 0x0fffffff

# variables globales
timer = 0
t2 = None
period = 1
f0_scalling = 0

def callback(line):
    """
    Fonction de callback appeler quand un evenement exterieur sur la pin parametrer en init.
    cette fonction permet de mesurer la durer d'une periode.
    :param line: voir documention upython.
    """
    global timer
    global t2
    global period
    
    tmp = t2.counter()
    period = tmp - timer
    timer = tmp

def raw_average(time_average=10):
    """
    La fonction raw_average permet de faire une moyenne des valeur brute lue sur une periode donnee
    :param time_average: Paremetre de temps qui definit la periode de temps sur laquelle on va effectuer la moyenne.
    :return: retourne la moyenne des valeur lue sur une periode de temps definit.
    """
    
    # boucle pour sommer les valeurs brutes
    for i in range(0, (time_average - 1)):
        sum += raw_measure()
        pyb.delay(1000)  # delais 1s
    
    # verification pour la division par zero
    try:
        return sum / time_average
    except ZeroDivisionError:
        print("division by zero, time average is bad, please change value")
        return -1

def raw_measure():
    """
    La fonction raw_measure renvoie la valeur brute d'ensoleillement du capteur en Hz
    :return: valeur mesurer par le capteur de PAR en Hz
    """
    
    global period
    
    # Test de la division par zero
    try:
        return 1000000 / period
    except ZeroDivisionError:
        print("division by zero, period is null, please check your wiring")
        return -1

# TODO en cour, amelioration, Beta
def uwatt_by_cm2_measure(raw_measure):
    """
    Fonction qui convertie la valeur brute du capteur en uwatt/cm2
    :return: la valeur convertie
    """
    global f0_scalling
    return ((raw_measure * f0_scalling) - DARK_FREQUENCY) / RESPONSIVITY


# TODO en cour, amelioration des facteur A et B, Beta
def Einstein_by_m2_by_second_measure(raw_measure):
    """
    Fonction qui donne la valeur d'ensoleillement en uE/m2/s
    :param raw_measure: valeur brute du capteur
    :return: Renvoie la valeur convertir en uE/m2/s
    """
    return ((raw_measure * FACOTR_A) + FACOTR_B)


def init(pin_name='X1', scalling=100):
    """
    Fonction d'inistilisation du capteur de par
    :param pin_name: identifiant du GPIO ou est connecter le capteur. par defaut la valeur et X1
    """
    global t2
    global f0_scalling
    
    f0_scalling = scalling  # valeur de scalling configurer sur le capteur
    
    # definition de la pin utiliser pas le capteur de par pour l'aquisition de donnée
    pin = pyb.Pin(pin_name, pyb.Pin.IN)
    pyb.Pin(pin)
    # parametrage du timer à 1 MHz.
    t2 = pyb.Timer(TIMER, prescaler=PRESCALER, period=PERIOD)
    # declaration d'une action sur evenement exterieur.
    pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_UP, callback)
    # ajout d'un delais de demarage au capteur pour avoir une valeur de mesure correcte
    pyb.delay(3000)  # delais 3s
