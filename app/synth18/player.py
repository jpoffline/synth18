import trackprogramming as tp
import reporting as report
import numpy as np
import samples as smp
import pyaudio
import config as t
import json

class PLAYER_PYADUDIO(object):
    def __init__(self):
        self._p = pyaudio.PyAudio()
        self._stream = self._p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=t.SAMPLERATE,
                        output=True)
        self._count = 1

    def write(self, sound):
        self._stream.write(sound)
        np.savetxt(t.DATASTORE + "waveform_" + str(self._count) + ".csv", sound, delimiter=",")
        self._count += 1

    def close(self):
        self._stream.stop_stream()
        self._stream.close()
        self._p.terminate()



class PLAYER(object):
    def __init__(self, trackfile):
        self._trackfile = trackfile
        self._logger = report.LOGGER()
        self._player = PLAYER_PYADUDIO()
        pass

    def play(self):
        ''' Play the sequencer'''
        self._load_and_play()

    def _load_and_play(self):

        self._logger.write('loading trackfile')
        trackfile = smp.load_trackfile(self._trackfile)

        self._logger.write('playing ' + trackfile['name'])
        sequences = tp.tracks_to_bin(trackfile['track'])

        tracks = trackfile['track']
        self._logger.write('generating samples')
        samples = smp.generatesamples()

        self._logger.write('playing')
        beatnum = 1
        for beat in sequences['sequences']:
            sound = (np.zeros(t.SAMPLERATE)).astype(np.float32)
            for track in xrange(0, len(tracks)):
                if beat[track]:
                    sound = np.add(sound, samples[sequences['names'][track]])
            self._player.write(sound)
            beatnum += 1

        self._player.close()

        self._logger.write('done')
