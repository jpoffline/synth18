
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
    