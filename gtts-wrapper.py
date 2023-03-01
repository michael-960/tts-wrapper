#!/usr/bin/python3

import os
import subprocess
import sys
import re
import pathlib
import json


p = pathlib.Path(__file__).resolve()

with open(p / 'config.json', 'r') as f:
    config = json.load(f)

gtts = config['gtts']
text = os.popen('xsel -b').read()

subs = [
    ('-\n', ''),
    ('\n', ' '),
    ('ϵ', ' epsilon '),
    ('ǫ', ' epsilon '),
    ('φ', ' phi '),
    ('χ', ' chi '),
    ('Ψ', ' psi '),
    ('Sec. ', ' section '),
    ('→', ' to '),
    ('/', ' over ')
]

for t, r in subs:
    text = text.replace(t, r)

# sentences = text.split('. ')
sentences = re.split('\. |, ', text)

for s in sentences:
    print(s)
    p_echo = subprocess.Popen(('echo', '-n', s), stdout=subprocess.PIPE)
    p_tts = subprocess.Popen((gtts, '-'), stdin=p_echo.stdout, stdout=subprocess.PIPE)
    p_audio = subprocess.Popen(('mpg123', '-'), stdin=p_tts.stdout)
    try:
        p_audio.wait()
    except KeyboardInterrupt:
        print('Interrupted')
        p_audio.kill()
        sys.exit(0)
    # os.system(f'echo -n "{s}" | {gtts} - | mpg123 - ')


