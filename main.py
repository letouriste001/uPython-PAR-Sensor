__author__ = "Christophe AUBERT"
__copyright__ = "Copyright 2016"
__credits__ = ["Christophe AUBERT"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Christophe AUBERT"
__status__ = "development"

import pyb
import TSL230RD


blueled=pyb.LED(4)
blueled.on()

# pas obligatoire on peux faire :
# TSL230RD.init
# et remplacer tout les par_sensor par TSL230RD

par_sensor = TSL230RD
par_sensor.init()

while 1:
    
    freq = par_sensor.raw_measure()
    print("Frequence : " + str(freq) + " Hz")
    einstein = par_sensor.Einstein_by_m2_by_second_measure(freq)
    print("PAR : " + str(einstein) + " uE/m2/s")
    uwatt = par_sensor.uwatt_by_cm2_measure(freq)
    print("PAR : " + str(uwatt) + " uW/m2/s")
    # attention il est important pour la mesure unique de mettre un delais de 1s entre chaque mesure
    pyb.delay(1000)
    
    # meme calcul mais avec la valeur moyenner sur 10 valeurs
    freq_a = par_sensor.raw_average(10)
    print("Frequence : " + str(freq_a) + " Hz")
    einstein = par_sensor.Einstein_by_m2_by_second_measure(freq_a)
    print("PAR : " + str(einstein) + " uE/m2/s")
    uwatt = par_sensor.uwatt_by_cm2_measure(freq_a)
    print("PAR : " + str(uwatt) + " uW/m2/s")
    