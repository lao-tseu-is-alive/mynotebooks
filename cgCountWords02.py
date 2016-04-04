#!/usr/bin/env python
from __future__ import print_function
from unicodedata import normalize
import locale
import re
import os
import datetime
d = datetime.datetime.now()
min_letters = 3

myFilename = "sample_data/Victor_Hugo-Les_miserables_Tome_1_UTF8.txt"
word_dict = {}
emptyLine_counter = 0
line_counter = 0

with open(os.path.expanduser(myFilename), mode='r') as myFile:
    lines = myFile.read()
print("Found a total of {nl} lines".format(nl=len(lines)))
wre = re.compile(ur'[^\s\n\t_.,;:\'"0123456789/()*+?!\u00AB\u00BB\-\[\]]+', re.UNICODE)
for line in lines:
    line_counter += 1
    print(line_counter )
    print(line)
    if len(line.strip()) > 0:
        for word in [w.lower().strip() for w in wre.findall(normalize('NFC', line.decode('utf8'))) if len(w) >= min_letters]:
            if len(word.strip()) > min_letters:
                if word.lower() in word_dict:
                    word_dict[word.lower()] += 1
                else:
                    word_dict[word.lower()] = 1
    else:
        emptyLine_counter += 1
print("with {nl}  empty lines, ".format(nl=emptyLine_counter))
print("and a total of {nw:} different words".format(nw=len(word_dict)))
print("having more then {} letters".format(min_letters))
# sort the  words by most used  ones
wordsByCount = sorted(((v, k) for k, v in word_dict.iteritems()), reverse=True)
for i in range(0, 50):
    print("{w:8} : {n}".format(w=wordsByCount[i][1].encode('utf-8'), n=wordsByCount[i][0]))


