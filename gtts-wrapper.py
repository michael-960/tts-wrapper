#!/home/michael/miniconda3/envs/tts/bin/python3
import os

gtts = '/home/michael/miniconda3/envs/tts/bin/gtts-cli'

text = os.popen('xsel').read()

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

sentences = text.split('. ')

for s in sentences:
    print(s)
    os.system(f'echo -n "{s}" | {gtts} - | mpg123 - ')

