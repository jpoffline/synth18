

import sys
import config
class LOGGER(object):
    def __init__(self):
        self.write('', prefix = '=======================')
        self.write(config.NAME, prefix = '  ')
        self.write('v' + config.VERSION, prefix = '     ')
        self.write('', prefix = '=======================')

        pass
        
    def write(self, msg, prefix = '* '):
        sys.stdout.write(prefix + str(msg) + '\n')
