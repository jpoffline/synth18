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

    sn       = t.SNAREDRUM(fac = 2.8)
    sn_short = t.SNAREDRUM(fac = 1)
    sn_db    = t.DOUBLESNARE()


    return {
        'bass': s1.get() * e.get() ,
        'snare': sn.get(),
        'snare_double': sn_db.get(),
        'a4':note_a4(),
        'bb4':note_bb4(),
        'b4':note_b4(),
        'c5':note_c5()
    }


def get_sine(freq = 440, duration = 0.2):
    sine = t.SINEWAVE(duration, freq)
    return sine.get()


def note_a4():
    return get_sine(440)
def note_bb4():
    return get_sine(466.16)
def note_b4():
    return get_sine(493.88)
def note_c5():
    return get_sine(523.25)
