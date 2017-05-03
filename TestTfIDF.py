#word_to_look_in1=raw_input("[+] Enter the word to see the frecvency: ")

#!/usr/bin/env python

"""
The simplest TF-IDF library imaginable.

Add your documents as two-element lists `[docname, [list_of_words_in_the_document]]` with `addDocument(docname, list_of_words)`. Get a list of all the `[docname, similarity_score]` pairs relative to a document by calling `similarities([list_of_words])`.

See the README for a usage example.
"""

from tfidf import tfidf

class TestTable:

    def __init__(self):
        self.performance = 0
        self.f = None
        self.wordfreq = []
        self.table = tfidf()
        self.listDictionaryFrecvency = []
        self.listDictionaries=[]
        self.file_dict = {}
        self.counter=0
        self.list={}
        self.keywords = ''
        print ('TEST tfIDF initiated')
        f = None
        self.f = open('output.txt', 'r')
        self.line = ''
        self.linesFile = 1


    # Given a list of objects, return a dictionary of
    # word-frequency pairs.
    def wordListToFreqDict(self, wordlist):
        wordfreq = [wordlist.count(p) for p in wordlist]
        return dict(zip(wordlist,wordfreq))
        

        
        
    # Sort a dictionary of word-frequency pairs in
    # order of descending frequency.
    def sortFreqDict(freqdict):
        aux = [(freqdict[key], key) for key in freqdict]
        aux.sort()
        aux.reverse()
        return aux
      
          
    #count  all lines  in file 
    def countFileLines(self, filename):
        lines = 0
        for line in open(filename):
            lines +=1
        
        print "\nThere are {} in the file".format(lines) 
        print "++++++++++++++++++++++++++++"
        return lines
        
        
    #count lines in one object
    def countLinesObject(self, filename):
        LinesObject=0
        for i in range(1,filename):
            LinesObject+=1
            if self.listDictionaries[i].keys()==['Title']:
                break
        print LinesObject
        return LinesObject
        
    #count lines in one object
    def setKeywords(self, keys):
        self.keywords = keys
        return
        
    #count lines in one object
    def getFrequency(self):
        return self.table.similarities (self.keywords)
    
    def updateFrequency(self, listObj):
        l = len(listObj)
        for i in range(0,l):
            excerptTitle = ''
            if('Excerpt' in listObj[i][0].keys()):
                excerptTitle = (listObj[i][0]['Excerpt'])
            if('Title' in listObj[i][0].keys()):
                excerptTitle += listObj[i][0]['Title']
            excerptTitle = excerptTitle.split()
            print excerptTitle
            self.table.addDocument("Document_{}".format(i), excerptTitle)
            #listDictionaryFrecvency.append(wordListToFreqDict(objectList.split()))
        print "List all object as dictionary at once!!!!\n"
        print self.table.similarities (self.keywords)
        
        for i in range(0, l):
            print
        
   
    #we create and array that has its lengh = to lines in file and each line is appended to it as a dictionary:
    #ie [{'Title': "Ara"},{'Year': '2000'},{}....]
    def arrayAllLinefile(self): 
        count=0
        objectList = []
        researchDict = {}
        linesFile = self.countFileLines("output.txt")
        line = self.f.read().splitlines()
        #index
        index = 0
        for i in range(linesFile):
            #objectListDict += line[i]
            if line[i] not in '\n':
                count+=1
            
                self.file_dict={line[i].split()[0]:line[i]}
                #print 'KEY VALUE \n'
                #print line[i].split()[0]
                key = line[i].split()[0]
                #print 'ACTUAL VALUE \n'
                #print file_dict[key]
                #print 'FILE DICT \n'
                #print file_dict
                #print 'FILE DICT 1 \n'
                
                #add file_dict to research dictionary object
                researchDict[key] = self.file_dict[key]
                
                self.file_dict={}
            
                #researchDict.append(file_dict)
                #researchDict[
                #objectListDict = " "
            else:
                #listDictionaries.append(file_dict)
                array = []
                #add empty performance value
                researchDict['Performance'] = 0.0
                array.append(researchDict.copy())
                print '-------------------Array---------------'
                print array
                objectList.append(array)
                self.file_dict={}
                researchDict.clear()
                index +=1
                
                
                #print listDictionaries
        return objectList
    
    def run(self):
        #linesFile = countFileLines("test2.txt")
        linesFile = self.countFileLines("output.txt")
        # check how many lines in one object  
        #countLinesObject(linesFile)
        list =  self.arrayAllLinefile()
        self.list = list
        print '----------------LIST OF RESEARCH DICT OBJECTS---------------/n'
        print list
        print '-------------------------------------------/n'
    
        
        l = len(list)
        print '----------LENGTH -----'
        print l
        for i in range(0,l):
            print i
            if('URL' in list[i][0].keys()):
                print list[i][0]['URL']
        
        print '----------------- GENERATE FREQUENCIES ------------'
        self.updateFrequency(list)

#print "========================================="
#t = TestTable()
#t.setKeywords("genome")
#t.run()