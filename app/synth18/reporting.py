

import sys

class LOGGER(object):
    def __init__(self):
        pass
        
    def write(self, msg):
        sys.stdout.write('* ' + str(msg) + '\n')
