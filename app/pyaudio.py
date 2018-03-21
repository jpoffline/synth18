
from flask import Flask, jsonify, render_template, request
import synth18.trackprogramming as tp
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
    import synth18.samples as smp
    tf = smp.load_trackfile(
            request.form['trackfilename'], root='tracks/')

    GLOBAL['trackfile'] = tf
    tf['html'] = tp.trackfile_to_html(tf)
    return render_template('index.html', trackprogramming = tf) 

@app.route("/play_track", methods =['POST'])
def play_track():
    print 'play track'
    print request.form['trackprog']
    d = dict(request.form)
    tp.parse_track_userinput(d)

    return render_static('index')


if __name__ == '__main__':
    app.run()