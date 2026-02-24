#!/usr/bin/env python3
"""Press to Reveal - 300 | Solution"""

def rot47(text):
    return ''.join(chr(33 + ((ord(c) - 33 + 47) % 94)) if 33 <= ord(c) <= 126 else c for c in text)

def keycodes_to_flag(keycodes):
    keymap = {48:'0',49:'1',50:'2',51:'3',52:'4',53:'5',54:'6',55:'7',56:'8',57:'9',
              65:'a',66:'b',67:'c',68:'d',69:'e',70:'f',72:'H',81:'Q',88:'X',
              219:'{',221:'}',187:'-',188:'-',189:'-'}
    skip = {17, 20, 27, 33, 34}
    return ''.join(keymap.get(k,'') for k in keycodes if k not in skip)

# Solve
with open('6a623F28F0file.enc') as f:
    decrypted = rot47(f.read())

import re
keycodes = [int(n) for n in re.findall(r'\d+', decrypted)[:47]]
flag = keycodes_to_flag(keycodes).replace('-','')

print(f"FLAG: {flag}")
