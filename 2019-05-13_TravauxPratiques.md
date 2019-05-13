# De la rétine à l'action: Modélisation des processus visuels

* Où: Marseille (France), see https://laurentperrinet.github.io/talk/2019-04-03-a-course-on-vision-and-modelization
* Quand: 13/05/2019, time: 13:00:00-18:00:00

* Quoi:
  * Slides @ https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization
  * Code for slides @ https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/

# Mainen & Sejnowski

## contexte
Le but de cette première tache est de créer un "raster plot" qui montre la reproducibilité d'un train de spike avec des répétitions du même stimulus, comme dans ce travail dans la [rétine de rongeurs](https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/#/1/3) ou dans le [cortex (V1) du chat](https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/#/1/6).

Ici, nous allons essayer de répliquer la figure 1 de [Mainen & Sejnowski (1995)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.299.8560&rep=rep1&type=pdf):

![Mainen Sejnowski 1995](http://i.stack.imgur.com/ixnrz.png "figure 1")

Et pour celà, nous allons procéder à plusieures étapes progressives:

## prise en main des outils: numpy et matplotlib

- on va créer des vecteurs représentant la dynamique d'un valeur en fonction du temps
- pour cela, on crée un vecteur `time' représentant 2 secondes avec une précision de dt=1ms
- dans un premier temps, on va créer un plot d'un spike, d'un créneau & d'une sinusoïde

## définition du problème: leaky-integrate and fire neuron

- on va simuler 1 neurone pour 2 secondes avec une précision de dt=1ms
- pour cela, on utilise l'équation d'un lIF
- on montre alors sa réponse aux stimuli créés ci-dessus

## injection d'un bruit

- Comme dans la figure 1 de Mainen & Sejnowski (1995), on ajoute un bruit à l'injection de courant
- ce bruit peut être caractisé par son amplitude et son temps caractéristique: quel est l'impact sur le résultat?
- que se passe-t-il quand on inclut un bruit interne à la dynamique du neurone?

## bonus: utilisation de pyNN / brian

- on va utiliser [brian](http://briansimulator.org/) pour écrire l'équation du lIF et refaire les mêmes simulations
- on compare avec d'autres modèles de neurone

## références

* http://e.guigon.free.fr/rsc/article/BretteGuigon03.pdf

# A selection of Izhikevich neurons

## contexte

Pour étendre notre répertoire de types de neurones, utilisons le formalisme de Eugene Izhikevich:

![An electronic version of the figure and reproduction permissions are freely available at www.izhikevich.com](http://people.ece.cornell.edu/land/courses/ece5760/DDA/AnallogSimIzhikevich/izhik.gif "phase space")

## simulations:

- Intrinsically bursting (IB) (reset_voltage=-55, reset_recovery=4)

- Chattering (CH) (reset_voltage=-50, reset_recovery=2)

- Fast spiking (FS) (tau_recovery=0.1)

- Low-threshold spiking (LTS) (coupling=0.25)

- Resonator (RZ) (tau_recovery=0.1, coupling=0.26)

## références

* https://www.nengo.ai/nengo/examples/advanced/izhikevich.html
* http://neuralensemble.org/docs/PyNN/examples/Izhikevich.html
