
import sys
import os
import subprocess
from tfidf import tfidf

class TestTfIDF:
    
    def __init__(self):
        self.f = None
        self.wordfreq = []
        print ('TEST tfIDF initiated')
    # Given a list of objects, return a dictionary of
    # word-frequency pairs.
    def wordListToFreqDict(self, wordlist):
        self.wordfreq = [wordlist.count(p) for p in wordlist]
        return dict(zip(wordlist, self.wordfreq))
    # Sort a dictionary of word-frequency pairs in
    # order of descending frequency.
    def sortFreqDict(self, freqdict):
        aux = [(freqdict[key], key) for key in freqdict]
        aux.sort()
        aux.reverse()
        return aux
    def line_count(self, filename):
        lines = 0
        for line in open(filename):
            lines += 1
        print lines
        print '+++++++++++++'
        return lines
    def calc(self, keywords):
        os.chdir(r'C:/Users/Ian/Desktop/scholar.py-master')
        f = open('output.txt', 'r')
        print ('line count %d' %  self.line_count('output.txt')) 
        lineCount = self.line_count('output.txt')
        line = f.read().splitlines()
        # objectList = " {} {} {} ".format(word_to_look_in1, word_to_look_in2, word_to_look_in3)
        objectList = " "
        m = 1  
        table = tfidf()
        #create objects from text file, 10 objects in our case
        for i in range(lineCount):
            objectList += line[i]
            if line[i] in '\n':
                print "\nHello empty\n"
                print objectList
                print "\n"
                print self.wordListToFreqDict(objectList.split())
                print ">>>>>>>>>>>>>>>>>>>>"
                print "Here start"
                print objectList.split()
                text =objectList.split()
                print "Here ends"
                table.addDocument(m, text)
                m+=1
                #print the freq of the entered words in each excert
                print "Here ends 2"
                #print "\nFreqvency of the {} in this excert is {}\n ".format(word_to_look_in1, wordListToFreqDict(objectList.split())[word_to_look_in1])
                #print "\nFreqvency of the {} in this excert is {}\n ".format(word_to_look_in2, wordListToFreqDict(objectList.split())[word_to_look_in2])
                #print "\nFreqvency of the {} in this excert is {}\n ".format(word_to_look_in3, wordListToFreqDict(objectList.split())[word_to_look_in3])
                print ">>>>>>>>>>>>>>>>>>>>"
                #objectList = ". {} {} {} ".format(word_to_look_in1, word_to_look_in2, word_to_look_in3)
        print "Here start 1"   
        # Words we add
        keys = keywords     
        print table.similarities (keys)
        
        
        if f is not None:
            f.close()
        return None
            
    #line_count(self, 'output.txt')
    #calculateBestPDF()
#tf = TestTfIDF()
#tf.calc()