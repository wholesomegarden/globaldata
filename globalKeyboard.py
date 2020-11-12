#globalKeyboard.py
import pynput
from pynput.keyboard import Key, Listener

from gd import *
mugic = xo.mugic
import time

last = time.time()
special = ["Key.ctrl","Key.alt","Key.shift","Key.cmd"]
keys = {}


import pygame

pygame.init()
sound = pygame.mixer.Sound("/home/magic/Downloads/piano1.wav")


def process(key, event):
    res = None
    if key in keys:
        kb = keys[key]
        if event is "press":
            if kb["last"] is "press" and time.time()-kb["press"][1] < 0.5:
                keys[key] = {"hold":[0,time.time()],"last":"hold"}

            elif kb["last"] is "hold":
                pass
            else:
                keys[key] = {event:[0,time.time()],"last":event}
                res = [key,1]

        if event is "release":
            if kb["last"] is "hold" or str(key) in special:
                keys[key] = {"release":[0,time.time()],"last":event}
                res = [key,2]
            keys[key] = {"release":[0,time.time()],"last":event}
    else:
        keys[key] = {event:[0,time.time()],"last":event}
        if event is "press":
            res = [key,1]

    if res is not None:
        print("RES",res)

    return res

def update(key, event):
    res = process(key,event)
    if res != None:
        if res[1] == 1:
            pygame.mixer.Sound.play(sound,loops=-1)
        if res[1] == 2:
            pygame.mixer.Sound.stop(sound)


        # mugic.play = res
        # print("!!!!!!!!!!!!!!!",mugic.play)

def on_press(key):
    # update(key, "press")


#
    global last
    print(time.time()-last,"last")
    last = time.time()
    # print('{0} pressed'.format(
    #     key))
    mugic.play = [key,1]
    # print(mugic.play.val[0])

def on_release(key):
    # update(key, "release")

    global last
    diff = time.time()-last
    last = time.time()
    print(diff,"last")
    if diff > 0.25:
        print('{0} release'.format(key))
        mugic.play = [key,2]
        print(mugic.play.val[0])
    if key == Key.esc:
        # Stop listener
        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
