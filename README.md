# uPython-PAR-Sensor

## Introduction
Cette librairie est écrite pour un capteur TSL 230 RD qui nous permet de mesurer le PAR
L’ensoleillement représente la mesure d’irradiance du PAR  (Photosynthetically active radiation). Le PAR est le rayonnement nécessaire à la photosynthèse qui se situe sur une plage de 400 à 700 nm de longueur d’onde , c’est à dire une grande partie du spectre du domaine visible (fig.1).

![Spectre électromagnétique](/images/spectre_electromagnetique.jpg)

Figure 1 Spectre électromagnétique, agrandissement sur le spectre visible. En noir, la partie du spectre visible non utilisée dans le PAR.

Pour mesurer la fiabilité du capteur TSL 230 RD on l’a comparé au capteur SUD033 couplet a un IL1700. Après une journée de mesure on obtient les courbes suivantes (fig.2)

![Courbe des capteurs](/images/courbe.png)

Figure 2 Graphique de mesure des capteurs IL1700 et TSL 230 RD

La courbe rouge a été mise à l’échelle d’un facteur trois pour mieux visualiser le fait que les deux courbes sont similaires.
On applique la régression linaire sur les valeurs des capteurs (fig.3).

![Régression linéaire](/images/reg_lin.png)

Figure 3 Représentation de la régression linaire entre les capteurs IL1700 et TSL230 RD

On constate après calcul que le coefficient de corrélation et de 94.4% ce qui est plutôt bon.
On utilisera les coefficient a et b pour calculer les valeur en μE m−2 s−1

Les conditions de test étant mauvais (coffret plexiglas abimer, alimentation non filtrer, etc.) (fig.4).

![Condition de test](/images/condition.jpeg)

Figure 4 Coffret de test du capteur de PAR premier test effectuer sur Arduino.

## Design PCB

Après les tests du capteur et dans un but d’amélioration de la lecture des valeurs j’ai réalisé ceci (fig.5) (les PCB sont disponibles sur le dépôt)*[]: 

![PCB](/images/PCB.png)

Figure 5 Photographie des pcb recto verso. En rouge la configuration de la sensibilité. En vert les pins de connexion et en Bleu une CTN pour correction de la valeur mesurer en fonction de la température.

## Adaptation pour Pyboard

En cour de rédaction

## Code d'exemple

En cour de rédaction

## Réference

En cour de rédaction

## English readme

Comming soon

## Copyright and Licence

En cour de rédaction