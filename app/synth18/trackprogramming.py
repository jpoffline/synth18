
def validate_trackvec(track_vec, req_ln = 16):
    return len(track_vec) == req_ln


def blowup_trackstring(track_string):

    track_string = track_string.replace(" ", "")
    track_beats = []
    for c in track_string:
        track_beats.append(c)
    if validate_trackvec(track_beats):
        return track_beats
    else:
        return 'track invalid length'


def trackvec_to_binary(track_vec):
    reply = []
    for beat in track_vec:
        if beat == "-":
            reply.append(False)
        else:
            reply.append(True)
    return reply


def tracks_to_bin(tracks):
    seqs = []
    smpln = []
    for k,v in tracks.iteritems():
        tracks[k]['vec'] = blowup_trackstring(tracks[k]['sequence'])
        tracks[k]['bin'] = trackvec_to_binary(tracks[k]['vec'])
        seqs.append(tracks[k]['bin'])
        smpln.append(tracks[k]['sample'])

    return { 'sequences':zip(*seqs), 'names':smpln }
    

def trackfile_to_html(tf):
    thtml = '<h2>Track programming</h2>'
    thtml += '<h3>' + tf['name'] + '</h3>'
    thtml += '<div class="container">'
    
    for tn, ti in tf['track'].iteritems():
        thtml += '<div class="row">'
        thtml += '<div class="col-1"><b>' + tn + '</b></div>' 
        thtml += '<div class="col-1">' + ti['sample'] + '</div>'
        thtml += '<div class="col-4">'
        tk = trackvec_to_binary(blowup_trackstring(ti['sequence']))
        n = 0
        for tki in tk:
            if tki:
                thtml += '<input type="checkbox" name="trackprog" value="' + tn + '-' + ti['sample'] + '-' + str(n) + '" checked>'
            else:
                thtml += '<input type="checkbox" name="trackprog" value="' +  tn + '-' + ti['sample'] + '-' + str(n) + '">'
            n = n + 1
        thtml += '</div></div>'
        
    return thtml +'</div>'



def parse_track_userinput(ui):

    track_ui = [i.split('-') for i in ui['trackprog']]
    ui_parsed = {}

    for tui in track_ui:
        track_name = tui[0]
        sample_name = tui[1]
        playit = int(tui[2])
        if not track_name in ui_parsed:
            ui_parsed[track_name] = {'sample':sample_name, 'sequence':[False for i in xrange(0,16)]}
        ui_parsed[track_name]['sequence'][playit] = True
    
    for k,v in ui_parsed.iteritems():
        s = ''
        for p in ui_parsed[k]['sequence']:
            if p:
                s += '+'
            else:
                s += '-'
        ui_parsed[k]['sequence'] = s

    return ui_parsed
