from alpha import Alphabet
from random import randint
import pyximport
pyximport.install()
from function import cycler

alphabet = Alphabet()

curr = []
for attrname in dir(alphabet):
    if attrname[0] != "_" and len(attrname) == 1:
        curr.append(alphabet.__getattribute__(attrname))
    elif attrname == "length":
        setlength = alphabet.__getattribute__(attrname)

shift = randint(1,26)
new = cycler(curr, setlength, shift)
print len(new)
new.append(alphabet.length)

for i, attrname in enumerate(dir(alphabet)):
    if attrname[0] != "_" and len(attrname) == 1:
        alphabet.__setattr__(attrname, new[i-18])

print alphabet.a, alphabet.length
