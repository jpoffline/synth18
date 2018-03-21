import waveforms as t
import envelopes as env

import json

def load_trackfile(filename, root = '../tracks/'):
    with open(root + filename + '.track') as json_data:
        d = json.load(json_data)
    return d

def generatesamples():
    
    e = env.ENVELOPE()
    duration = 0.2

    s1 = t.SINEWAVE(duration, 280)
    s2 = t.SINEWAVE(duration, 290)
    s3 = t.SINEWAVE(duration, 2040)
    s4 = t.SINEWAVE(duration, 4000)

    

    whitenoise = t.WHITENOISE()

    sn       = t.SNAREDRUM(fac = 2.8)
    sn_short = t.SNAREDRUM(fac = 1)
    sn_db    = t.DOUBLESNARE()


    s2 = {
        'bass': (s1.get()  ) * e.get() ,
        'sample2':s2.get() * e.get(),
        'snare':sn.get(),
        'snare_double': sn_db.get()
    }
    return s2
