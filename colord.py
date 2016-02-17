from rc import recog
from pocketsphinx import *
import sys
import os


model = sys.argv[1]

pwd = os.path.abspath(os.curdir)

config = Decoder.default_config()

# custom config
#hmdir = '/usr/local/share/pocketsphinx/model/en-us/en-us'
#lmd   = os.path.join(pwd, '{0}.lm'.format(model))
#dictd  = os.path.join(pwd, '{0}.dic'.format(model))
#config.set_string('-hmm', hmdir)
#config.set_string('-lm', lmd)
#config.set_string('-dict', dictd)



# copy pasta config
MODELDIR = '/usr/local/share/pocketsphinx/model/'
config.set_string('-hmm', os.path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', os.path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', os.path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))


log = os.path.join(pwd, 'output.log')
config.set_string('-logfn', log)

decoder = Decoder(config)

wavfile = 'myfile.wav'

print recog(wavfile, decoder)
