from rc import recog
from pocketsphinx import *
import sys

model = sys.argv[1]


config = Decoder.default_config()
hmdir = '/usr/local/share/pocketsphinx/model/en-us/en-us'
lmd   = '/mnt/data/madalyn/{0}.lm'.format(model)
dictd = '/mnt/data/madalyn/{0}.dic'.format(model)
log = '/mnt/data/madalyn/output.log'
print lmd
config.set_string('-hmm', hmdir)
config.set_string('-lm', lmd)
config.set_string('-dict', dictd)
config.set_string('-logfn', log)

decoder = Decoder(config)
# decoder.start_utt()

wavfile = 'fucking-goddamn-shit.wav'

print recog(wavfile, decoder)
