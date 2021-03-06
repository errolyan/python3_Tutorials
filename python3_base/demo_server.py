# /usr/local/bin python
# coding="utf-8"
# __author__="ErrolYan"
# __Describe__="web_server"


import os
import io,wave
import argparse
import librosa.filters
import falcon
import scipy
import numpy as np
from wsgiref import simple_server
import subprocess



html_body = '''<html><title>Mandarin TTS using end to end </title>
<style>

body {padding: 16px; font-family: sans-serif; font-size: 14px; color: #444}
input {font-size: 14px; padding: 8px 12px; outline: none; border: 1px solid #ddd}
input:focus {box-shadow: 0 1px 2px rgba(0,0,0,.15)}
p {padding: 12px}
button {background: #28d; padding: 9px 14px; margin-left: 8px; border: none; outline: none;
        color: #fff; font-size: 14px; border-radius: 4px; cursor: pointer;}
button:hover {box-shadow: 0 1px 2px rgba(0,0,0,.15); opacity: 0.9;}
button:active {background: #29f;}
button[disabled] {opacity: 0.4; cursor: default}
</style>
<body>
<form>
  <input id="text" type="text" size="40" placeholder="Enter Text">
  <button id="button" name="synthesize">Speak</button>
</form>
<p id="message"></p>
<audio id="audio" controls autoplay hidden></audio>
<script>
function q(selector) {return document.querySelector(selector)}
q('#text').focus()
q('#button').addEventListener('click', function(e) {
  text = q('#text').value.trim()
  if (text) {
    q('#message').textContent = 'Synthesizing...'
    q('#button').disabled = true
    q('#audio').hidden = true
    synthesize(text)
  }
  e.preventDefault()
  return false
})
function synthesize(text) {
  fetch('/synthesize?text=' + encodeURIComponent(text), {cache: 'no-cache'})
    .then(function(res) {
      if (!res.ok) throw Error(res.statusText)
      return res.blob()
    }).then(function(blob) {
      q('#message').textContent = ''
      q('#button').disabled = false
      q('#audio').src = URL.createObjectURL(blob)
      q('#audio').hidden = false
    }).catch(function(err) {
      q('#message').textContent = 'Error: ' + err.message
      q('#button').disabled = false
    })
}
</script></body></html>
'''


class UIResource:
  def on_get(self, req, res):
    res.content_type = 'text/html'
    res.body = html_body


class SynthesisResource:
  def merlinSynthersizer(self,text):
    #subprocess.call(["bash", "./merlin_synthesis.sh", text])
    outWav = "./audio/wav"
    wav = librosa.core.load(outWav, sr=48000)[0]
    print(wav)
    out = io.BytesIO()
    # print(out)
    # wf=wave.open(outWav,'rb')
    # print(wf)
    # data = wf.readframes(1024)
    # print(data)
    scipy.io.wavfile.write(out, 48000, wav.astype(np.int16))
    print(out.getvalue())
    return out.getvalue()


  def on_get(self, req, res):
    if not req.params.get('text'):
      raise falcon.HTTPBadRequest()
    print(req.params.get('text'))
    res.data = self.merlinSynthersizer(req.params.get('text'))
    res.content_type = 'audio/wav'


api = falcon.API()
api.add_route('/synthesize', SynthesisResource())
api.add_route('/', UIResource())


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--port', type=int, default=9000)
  args = parser.parse_args()
  print('Serving on port %d' % args.port)
  simple_server.make_server('0.0.0.0', args.port, api).serve_forever()
