from phue import Bridge
import random
from helper import D

b = Bridge(D['light_ip'])
#b.connect()
    
b.set_light(1, 'xy', [random.random(),random.random()])


