
from flask import Flask, jsonify, render_template, request
import synth18.trackprogramming as tp
import synth18.player as player
import synth18.samples as smp

app = Flask(__name__)

GLOBAL = {}


@app.route('/')
def index():
    return render_static('index')

def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route("/start_playing", methods=['POST'])
def echo():
    return render_template('index.html', name = request.form['text']) 

@app.route("/load_trackfile", methods=['POST'])
def loadtrackfile():
    
    tf = smp.load_trackfile(
            request.form['trackfilename'], root='tracks/')

    GLOBAL['trackfile'] = tf
    
    tf['html'] = tp.trackfile_to_html(tf)
    return render_template('index.html', trackprogramming = tf) 

@app.route("/play_sine", methods=['POST'])
def play_sine():
    d = dict(request.form)
    
    plyr = player.PLAYER()
    plyr.play_sample(smp.get_sine(float(d['sinefreq'][0])))
    return render_template('index.html')


@app.route("/play_track", methods =['POST'])
def play_track():
    print 'play track'
    
    d = dict(request.form)
    tr = tp.parse_track_userinput(d)

    plyr = player.PLAYER()
    plyr.set_tracks(tr)
    plyr._play_samples_sequences()
    tf = {'track':tr, 'name':GLOBAL['trackfile']['name']}
    
    tf['html'] = tp.trackfile_to_html(tf)

    return render_template('index.html', trackprogramming = tf)




if __name__ == '__main__':
    app.run()