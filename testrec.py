
import sys

import numpy as np
import sounddevice as sd


SAMPLE_RATE = 44100
CHANNELS = 1

import numpy as np
from scipy.io.wavfile import write

# Samples per second
sps = 44100

# Frequency / pitch of the sine wave
freq_hz = 440.0

# Duration
duration_s = 5.0

# NumpPy magic
each_sample_number = np.arange(duration_s * sps)
waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32767)

# Write the .wav file
# write('test.wav', sps, waveform_integers)


def record(filename, duration, index):
    sd.default.device = index
    my_recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS)
    write('test.wav', sps, my_recording)
    sd.wait()
    sd.play(my_recording, SAMPLE_RATE)
    sd.wait()
    # np.save(filename, my_recording)


if __name__ == '__main__':
    filename = sys.argv[1]
    duration = 3
    c=-1
    while(c<20):
        try:
            c+=1
            record(filename, duration,index = c)
        except Exception as e:
            print("EEEEEE",c,e)
