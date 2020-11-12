#MugicKeyboard.py
#globalKeyboard.py
import pynput
from pynput.keyboard import Key, Listener

from gd import *
mugic = xo.mugic
import time

last = time.time()
special = ["Key.ctrl","Key.alt","Key.shift","Key.cmd"]
keys = {}

import sounddevice as sd
fs = 44100

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

#0
#9
#11

sd.default.device = 16

myrecording = None
def update(key, event):
    global myrecording
    res = None
    print(str(key))
    if "p" in str(key) and "Key" not in str(key):
        print("!!!!!!PPPPPPPPPPP!!!!!!")
        sd.stop()
        sd.play(myrecording, fs)

    elif 'r'in str(key) and "Key" not in str(key):
        print("!!!!!!RRRRRR!!!!!!")
        duration = 1
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        # myrecording = sd.playrec(myrecording, fs, channels=2)

    else:
        res = process(key,event)

    if res != None:
        if res[1] == 1:
            pygame.mixer.Sound.play(sound,loops=-1)
        if res[1] == 2:
            pygame.mixer.Sound.stop(sound)


        # mugic.play = res
        # print("!!!!!!!!!!!!!!!",mugic.play)

def on_press(key):

    update(key, "press")


def on_release(key):
    update(key, "release")



with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
