import waveforms as t

def loadsamples():
    
    e = t.ENVELOPE()
    duration = 0.2

    s1 = t.SINEWAVE(duration, 240)
    s2 = t.SINEWAVE(duration, 480)
    s3 = t.SINEWAVE(duration, 2040)

    s4 = t.SINEWAVE(duration, 4000)

    sample1 = s1.get() * e.get()
    sample2 = s2.get() * e.get()
    sample3 = s3.get() * e.get()

    
    
    sn = t.SNAREDRUM(fac = 2.5)
    sn_short = t.SNAREDRUM(fac = 1)
    snare = sn.get()


    s2 = {
        'bass': sample1,
        'sample2':sample2,
        'snare':snare,
        'snare_short': sn_short.get()
    }
    return s2
