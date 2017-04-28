#word_to_look_in1=raw_input("[+] Enter the word to see the frecvency: ")

#!/usr/bin/env python

"""
The simplest TF-IDF library imaginable.

Add your documents as two-element lists `[docname, [list_of_words_in_the_document]]` with `addDocument(docname, list_of_words)`. Get a list of all the `[docname, similarity_score]` pairs relative to a document by calling `similarities([list_of_words])`.

See the README for a usage example.
"""

import sys
import os

class tfidf:
  def __init__(self):
    self.weighted = False
    self.documents = []
    self.corpus_dict = {}

  def addDocument(self, doc_name, list_of_words):
    # building a dictionary
    doc_dict = {}
    for w in list_of_words:
      doc_dict[w] = doc_dict.get(w, 0.) + 1.0
      self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0

    # normalizing the dictionary
    length = float(len(list_of_words))
    for k in doc_dict:
      doc_dict[k] = doc_dict[k] / length

    # add the normalized document to the corpus
    self.documents.append([doc_name, doc_dict])

  def similarities(self, list_of_words):
    """Returns a list of all the [docname, similarity_score] pairs relative to a list of words."""

    # building the query dictionary
    query_dict = {}
    for w in list_of_words:
      query_dict[w] = query_dict.get(w, 0.0) + 1.0

    # normalizing the query
    length = float(len(list_of_words))
    for k in query_dict:
      query_dict[k] = query_dict[k] / length

    # computing the list of similarities
    sims = []
    for doc in self.documents:
      score = 0.0
      doc_dict = doc[1]
      for k in query_dict:
        if k in doc_dict:
          score += (query_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
      sims.append([doc[0], score])

    return sims
    
 
f = None
try:
    f = open('output.txt', 'r')
    
    # create a counter to count the objects that are the snippets of 10 docs    
    table = tfidf()
    
    listDictionaryFrecvency = []
    listDictionaries =[]
    #arrayListObject=[0,0,0,0,0,0,0,0,0,0]
    
    file_dict = {}
    counter=0 

                    

    line = f.read().splitlines()
    objectList = " "
    

    # Given a list of objects, return a dictionary of
    # word-frequency pairs.
    def wordListToFreqDict(wordlist):
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
    def countFileLines(filename):
        lines = 0
        for line in open(filename):
            lines +=1
        
        print "\nThere are {} in the file".format(lines) 
        print "++++++++++++++++++++++++++++"
        return lines
        
        
   #count lines in one object 
    def countLinesObject(filename):
        LinesObject=0
        for i in range(1,filename):
            LinesObject+=1
            if listDictionaries[i].keys()==['Title']:
                break
        print LinesObject
        return LinesObject
    
    #linesFile = countFileLines("test2.txt")
    linesFile = countFileLines("output.txt")
    
    def updateFrequency(listObj):
        l = len(list)
        for i in range(0,l):
            excerptTitle = ''
            if('Excerpt' in list[i][0].keys()):
                excerptTitle = (list[i][0]['Excerpt'])
            if('Title' in list[i][0].keys()):
                excerptTitle += list[i][0]['Title']
            excerptTitle = excerptTitle.split()
            print excerptTitle
            table.addDocument("Document_{}".format(i), excerptTitle)
            #listDictionaryFrecvency.append(wordListToFreqDict(objectList.split()))
        print "List all object as dictionary at once!!!!\n"
        print table.similarities (['relativity', 'composition'])
        
        for i in range(0, l):
            print
        

    print "========================================="
   
    #we create and array that has its lengh = to lines in file and each line is appended to it as a dictionary:
    #ie [{'Title': "Ara"},{'Year': '2000'},{}....]
    def arrayAllLinefile(): 
        count=0
        objectListDict=''
        objectList = []
        researchDict = {}
        #index
        index = 0
        for i in range(linesFile):
            
            #objectListDict += line[i]
            if line[i] not in '\n':
                count+=1
            
                file_dict={line[i].split()[0]:line[i]}
                #print 'KEY VALUE \n'
                #print line[i].split()[0]
                key = line[i].split()[0]
                #print 'ACTUAL VALUE \n'
                #print file_dict[key]
                #print 'FILE DICT \n'
                #print file_dict
                #print 'FILE DICT 1 \n'
                
                #add file_dict to research dictionary object
                researchDict[key] = file_dict[key]
                
                file_dict={}
            
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
                file_dict={}
                researchDict.clear()
                index +=1
                
                
                #print listDictionaries
        return objectList
        
    # check how many lines in one object  
    #countLinesObject(linesFile)
    list =  arrayAllLinefile()
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
    updateFrequency(list)
        
    
    """
    count2=0
    count3=0
    # create a aray of lengh 10 as the # of docs we have each aray[i] will contain a dictionary as a object:
    #ie [{'Title': "Ara",'Year': '2000','Citation':'Blabla'}..., {'Title': "Night",'Year': '2012',...}, etc.]
    # agian we substract -10 since we have 10 empty  lines
    for i in range(linesFile-10):
        
        # each object strats with the key-> 'Title'
        if listDictionaries[i].keys()==['Title']:
            
            for j in range(10):
                print "this is count2 {}".format(count2)
                print "this is count3 {}".format(count3)
                print "this is J {}".format(j)
                #arrayListObject[j]=listDictionaries[i]
                #print arrayListObject[j]
                count3+=1
                count2+=1
            count3=0
            print "Here "
            
    print arrayListObject      
    # we aubstract 10 since we have 10 empty line and we dont want them        
    for i in range(linesFile-10):
        print listDictionaries[i]
          
    #print  listDictionaryLine
    #create objects from text file, 10 objects that we are geting form gooogle scholar
    for i in range(linesFile):
        objectList += line[i]
    """   
    """
        if line[i] in '\n':
            
            print "\nEmpty line here---------------------------------\n"
            print "\nHere we start loop....................................\n"
            print "Printing the original text doc\n{}\n". format(objectList)
            print "Printing the list of words from the doc as a list of strings\n{}\n".format(objectList.split())
            print "Printing the frecvency of each word in doc\n{}\n".format(wordListToFreqDict(objectList.split()))
            text =objectList.split()
            #adding docs to the table to do the similarity thing
            table.addDocument("Document_{}".format(counter), text)
            counter+=1
            #creating a list of dictonary frecvency for each objects: [{the:3,a:9}, {the: 20, a: 1100}]
            listDictionaryFrecvency.append(wordListToFreqDict(objectList.split()))
            
           
            #print the freq of the entered words in each excert
            print "n\Here we end loop\n"
            objectList = " "
 

    print "List all object as dictionary at once!!!!\n"
    #print listDictionaryFrecvency
    
    print "\nPrint the object as dictionaty from the 8th doc\n"
    print listDictionaryFrecvency[7]
    
    print "\nPrint the key:->> bioinformatics and its frecvency from 1st doc\n"
    print (listDictionaryFrecvency[0]['bioinformatics'])
    
    print "\nPrint the key:->> bioinformatics and its frecvency from 2st doc\n"
    print (listDictionaryFrecvency[1]['bioinformatics'])    
    
    print "\nPrint the object as dictionaty from the 10th doc\n"
    print listDictionaryFrecvency[9]
    
    print "\nHere we print similarity for Documents \n"        
    print table.similarities (['Title', 'genome', 'bioinformatics'])
    print "\n"

    """  
    
finally:
    if f is not None:
       f.close()