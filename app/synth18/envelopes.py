
import numpy as np
import config as t
SAMPLERATE = t.SAMPLERATE

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