import os
from functools import reduce
rb = bytes([114,98]).decode()
wb = bytes([119,98]).decode()
reps = [(bytes([0xe2,0x80,0x9c]),bytes([34])),(bytes([0xe2,0x80,0x9d]),bytes([34])),(bytes([0xe2,0x80,0x98]),bytes([39])),(bytes([0xe2,0x80,0x99]),bytes([39])),(bytes([0xe2,0x80,0xa6]),bytes([46,46,46])),(bytes([0xe2,0x80,0x93]),bytes([45])),(bytes([0xe2,0x80,0x94]),bytes([45]))]
exts = (bytes([46,106,115,120]).decode(),bytes([46,106,115]).decode(),bytes([46,116,115,120]).decode(),bytes([46,116,115]).decode())
allfiles = [os.path.join(r,f) for r,d,fs in os.walk(bytes([46]).decode()) for f in fs if f.endswith(exts) and bytes([110,111,100,101,95,109,111,100,117,108,101,115]).decode() not in r]
[open(p,wb).write(reduce(lambda t,rv: t.replace(rv[0],rv[1]),reps,open(p,rb).read())) for p in allfiles]
print(allfiles)
