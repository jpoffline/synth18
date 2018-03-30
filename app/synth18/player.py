import json
import numpy as np
import pyaudio

import synth18.trackprogramming as tp
import synth18.reporting as report
import synth18.samples as smp
import synth18.config as t


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
    def __init__(self, trackfile=None):
        self._trackfile = trackfile
        self._logger = report.LOGGER()
        self._player = PLAYER_PYADUDIO()
        self._sequences = None
        self._tracks = None
        self._samples = None
        pass

    def play(self):
        ''' Play the sequencer'''
        self._load_and_play()

    def _load_and_play(self):

        self._logger.write('loading trackfile')
        trackfile = smp.load_trackfile(self._trackfile)

        self._logger.write('playing ' + trackfile['name'])
        

        self.set_tracks(trackfile['track'])
        self._play_samples_sequences()

        self._logger.write('done')

    def set_sequences(self, seq):
        self._sequences = seq
        
    def set_tracks(self, tr):
        self._tracks = tr
        self.set_sequences(tp.tracks_to_bin(tr))

    def gen_samples(self):
        self._logger.write('generating samples')
        self._samples = smp.generatesamples()


    def _play_samples_sequences(self):
        self.gen_samples()

        self._logger.write('playing')
        beatnum = 1
        for beat in self._sequences['sequences']:
            sound = (np.zeros(t.SAMPLERATE)).astype(np.float32)
            for track in xrange(0, len(self._tracks)):
                if beat[track]:
                    sound = np.add(sound, self._samples[self._sequences['names'][track]])
            self._player.write(sound)
            beatnum += 1

        self._player.close()

    def play_sample(self, sample):
        self._player.write(sample)
        self._player.close()
