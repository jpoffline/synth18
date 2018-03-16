
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_static('index')

def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route("/start_playing", methods=['POST'])
def echo():
    return render_template('index.html', name = request.form['text']) 


@app.route("/opts", methods=['POST'])
def echo2():
    d = dict(request.form)
    pads_active = d['pad-tick']
    print pads_active
    return render_template('index.html', name = 'jonny') 

if __name__ == '__main__':
    app.run()