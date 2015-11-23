#!/usr/bin/env python
__author__ = 'cgil'
import os
import datetime
import re
d = datetime.datetime.now()
min_letters = 3

myFilename = "~/sample_data/VictorHugo_Les_miserables_UTF8.txt"
word_dict = {}
emptyLine_counter = 0
line_counter = 0

with open(os.path.expanduser(myFilename), mode='r') as myFile:
    txt = myFile.read()
print("Found a total of {nl} lines".format(nl=len(lines)))
for line in lines:
    line_counter += 1
    if len(line.strip()) > 0:
        for word in re.split(r"[ ',\n]+", line.decode('utf-8')):
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


