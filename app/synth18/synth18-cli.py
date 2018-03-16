
#import test
import trackprogramming as tp
import reporting as report
import numpy as np
import samples as smp
import pyaudio
import test as t

logger = report.LOGGER()

ds = '/Users/jap/scratch/pyaudio/data-synth18/'

tracks = {
    'track1':{
        'sequence':" - + + + - + + + ",
        'sample': 'snare'
    },
    'track2':{
        'sequence':" + - + - + - + - ",
        'sample': 'bass'
    },
    'track3':{
        'sequence':" + - + - + - + - ",
        'sample': 'snare_short'
    }
}

blah = tp.tracks_to_bin(tracks)

s2 = smp.loadsamples()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=t.SAMPLERATE,
                output=True)

beatnum = 1
for beat in blah['bin']:
    sound = (np.zeros(t.SAMPLERATE)).astype(np.float32)
    for track in xrange(0,len(tracks)):
        if beat[track]:
            sound = np.add(sound,s2[blah['names'][track]])
    stream.write(sound)
    np.savetxt(ds + "waveform_" + str(beatnum) + ".csv", sound, delimiter=",")
    beatnum +=1



stream.stop_stream()
stream.close()
p.terminate()

