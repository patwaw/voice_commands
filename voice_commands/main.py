# voice_commands version 0.1
# using google voice api
# 
# TODO: recoding to 16000Hz encoded FLAC(max 15 second recording)
# TODO: add commands to execute
# TODO: error handling

import urllib2
import sys
import json

URL = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US'
HEADER = {'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}

sound = open(sys.argv[1], 'r').read()

request = urllib2.Request(URL, data=sound, headers=HEADER)
response = urllib2.urlopen(request)
result = response.read()
print json.loads(result)['hypotheses'][0]['utterance']