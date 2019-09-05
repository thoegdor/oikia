import random
from os import listdir

def pic_chooser():
    
    pics_dir = 'pics/'
    pics_list = listdir(pics_dir)

    the_choice = pics_dir + random.choice(pics_list)
    return(the_choice)
