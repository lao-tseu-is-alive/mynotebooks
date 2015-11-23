from __future__ import print_function
from unicodedata import normalize
import locale
import re


def read_non_empty_lines_as_array(file_path):
    '''
        will return a list containing all non empty lines inside file_path text file
        :param file_path: a string containing the path to a text file
        :return: a list with all the non empty lines (strip applied)
    '''
    fc = []
    for l in open(file_path, mode='r'):
        if len(l.strip()) > 0:
            fc.append(l.strip())
    return fc


def read_as_text(filepath):
    '''
        will return the text inside the filepath text file
        :param filepath: a string containing the path to a text file
        :return: the text inside the file
    '''
    with open(filepath, mode='r') as myFile:
        return myFile.read()


def get_words_as_list(text, min_length):
    '''
    will return the list of words in text greater then minlen chars
    :param text: the test to analyse
    :param min_length: the minimum length to keep the word
    :return:
    '''
    wre = re.compile(ur'[^\s\n\t_.,;:\'"0123456789/()*+?!\u00AB\u00BB\-\[\]]+', re.UNICODE)
    return [w.lower().strip() for w in wre.findall(normalize('NFC', text.decode('utf8'))) if len(w) >= min_length]


def get_unique_words_in_file1(file_path, min_length):
    wre = re.compile(ur'[^\s\n\t_.,;:\'"0123456789/()*+?!\u00AB\u00BB\-\[\]]+', re.UNICODE)
    words = [word.strip().lower() for line in open(file_path, mode='r')
             for word in wre.findall(normalize('NFC', line.decode('utf8'))) if len(line.strip()) > 0]
    words = [w for w in words if len(w) >= min_length]
    words_unique = list(set(words))
    locale.setlocale(locale.LC_ALL, '')
    words_unique.sort(cmp=locale.strcoll)
    print("num unique words : {nw} ".format(nw=len(words_unique)))
    print("head : ", *words_unique[1:25], sep=' - ')
    print("tail : ", *words_unique[len(words_unique)-25:], sep=' - ')
    return words_unique


def get_unique_words_in_file2(file_path, min_length):
    text = read_as_text(file_path)
    words = get_words_as_list(text, min_length)
    words_unique = list(set(words))
    locale.setlocale(locale.LC_ALL, '')
    words_unique.sort(cmp=locale.strcoll)
    print("num unique words : {nw} ".format(nw=len(words_unique)))
    print("head : ", *words_unique[1:25], sep=' - ')
    print("tail : ", *words_unique[len(words_unique)-25:], sep=' - ')
    return words_unique


if __name__ == "__main__":
    from timeit import Timer
    myFilename = "sample_data/VictorHugo_Les_miserables_UTF8.txt"
    t1 = Timer("get_unique_words_in_file1(myFilename, 3)",
               setup="from __main__ import get_unique_words_in_file1,myFilename")
    t1.timeit(1)
    t1.print_exc()
    t2= Timer("get_unique_words_in_file2(myFilename, 3)",
              setup="from __main__ import get_unique_words_in_file2,myFilename")
    t2.timeit(1)
    t2.print_exc()

