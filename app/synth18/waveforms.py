

import numpy as np
import config as t
SAMPLERATE = t.SAMPLERATE

class SAMPLE(object):
    def __init__(self, duration, f, fs = SAMPLERATE):
        #fs = sampling rate (Hz)
        self._sample_rate = fs
        self._duration = duration
        self._frequency = f
        pass

    def get(self):
        pass

class SINEWAVE(SAMPLE):
    def get(self):
        vals = [0.2*np.sin(2*np.pi*i*self._duration*self._frequency / SAMPLERATE) for i in xrange(0,SAMPLERATE)]
        return np.array(vals).astype(np.float32)


class ENVELOPE(object):
    def __init__(self):
        self._attack = 0
        self._decay = 0.95

    def get(self):
        cut = int(self._decay*SAMPLERATE )
        vals = [1 for i in xrange(0, SAMPLERATE)]
        m = -1.0 / (SAMPLERATE - self._decay*SAMPLERATE)
        c = -m * SAMPLERATE 
        d =  1 
        
        vals[cut:SAMPLERATE] = [m * d * i + c for i in xrange(cut, SAMPLERATE)]
        
        return np.array(vals).astype(np.float32)


class SNAREDRUM(object):
    def __init__(self, fac = 1):
        self._decay = 0.001 / fac
    def get(self):
        env = WHITENOISE()
        vals = [np.exp(-self._decay * i) for i in xrange(0, SAMPLERATE)]
        return np.array(vals).astype(np.float32) * env.get()

class DOUBLESNARE(object):
    def __init__(self, fac = 1):
        self._decay = 0.001 / fac
    def get(self):
        env = WHITENOISE()
        vals = [np.exp(-self._decay * i) for i in xrange(0, SAMPLERATE / 2)]
        vals[SAMPLERATE / 2:SAMPLERATE] = [np.exp(-self._decay * i) for i in xrange(0, SAMPLERATE / 2)]
        return np.array(vals).astype(np.float32) * env.get()

class WHITENOISE(object):
    def __init__(self):
        pass
        
    def get(self):
        b = -0.2
        a = 0.2
        
        vals = [(b - a) * np.random.random_sample() + a for i in xrange(0, SAMPLERATE)]
        return np.array(vals).astype(np.float32)
