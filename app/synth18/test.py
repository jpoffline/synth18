
import pyaudio
import time
import math
from itertools import count
import numpy as np
SAMPLERATE = 44100
#SAMPLERATE = 10

if False:
    p = pyaudio.PyAudio()

    volume = 0.5     # range [0.0, 1.0]

    duration = 0.1   # in seconds, may be float
    f = 440.0        # sine frequency, Hz, may be float

    sample1 = SINEWAVE(duration, f)

    # generate samples, note conversion to float32 array
    samples = sample1.get()



    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=SAMPLERATE,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(samples)
    #stream.write(samples2)

    stream.stop_stream()
    stream.close()

    p.terminate()