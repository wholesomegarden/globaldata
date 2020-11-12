#MugicKeyboard.py

from gd import *
import pygame


import pyaudio
import numpy as np


# Collect events until released
fs = 44100

def tone(volume = 0.5,     # range [0.0, 1.0]
fs = 44100,      # sampling rate, Hz, must be integer
duration = 3.0,   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float
):
# generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()
    return samples


# play. May repeat with different volume values (if done interactively)

from threading import Thread


playing = {}

def startStreamThread(kb):
    global playing

    freq = tone(f = 440.0 * (1+len(playing.keys())))
    print(kb,"!!!!!!")
    print("STARTING STREAM")
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    playing[kb] = stream
    t = Thread(target = startStream, args = [stream,freq])
    t.start()
    return stream

def startStream(stream,tone):
    # stream, tone = data
    print("STARTING STREAM")
    stream.write(tone)


def stopStreamThread(kb):
    global playing
    print("STOPING STREAM")
    if kb in playing:
        t = Thread(target = stopStream, args = [playing[kb]])
        t.start()
        playing.pop(kb)


def stopStream(stream):
    print("STOPING STREAM")
    stream.stop_stream()


mugic = xo.mugic

pygame.init()
sound = pygame.mixer.Sound("/home/magic/Downloads/piano1.wav")

def init():
    mugic.play = ["x",0]
    musicloop()


def musicloop():
    p = pyaudio.PyAudio()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = None
    while(True):
        c = 0
        lastkb = ""
        while(mugic.play.val[0][1] == 1):
            if mugic.play.val[0][0] != lastkb:
                c = 0
            lastkb = mugic.play.val[0][0]
            c+=1
            if c == 1:
                print("111111111111111")
                pygame.mixer.Sound.play(sound,loops=-1)

                # stream = startStreamThread(mugic.play.val[0][0])
                # stream.write(tone())
            # print(mugic.play.val[0])

            # mugic.show()
        # pygame.mixer.Sound.stop(sound)
        if mugic.play.val[0][1] == 2:
            pygame.mixer.Sound.stop(sound)
            mugic.play.val[0][1] = 3
            # stream.write(samples)
            stopStreamThread(mugic.play.val[0][0])
            # stream.stop_stream()

        # mugic.show()
        # print(mugic.play.val[0])



    stream.close()
    p.terminate()


if __name__ == '__main__':
    p = pyaudio.PyAudio()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    # samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # print("!!!!!!!!!!!")
    # stream.write(tone())
    # print("@@@@@@@@@@@")
    # stream.stop_stream()

    # stream.close()
    # p.terminate()

    init()
