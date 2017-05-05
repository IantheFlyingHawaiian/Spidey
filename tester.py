from bs4 import BeautifulSoup
import scholar
import sys, getopt, os
#from pdf2text import convert_pdf_to_txt
from tfidf import tfidf
from TestTfIDF import TestTable
import time
from kmeans import KmeansTest
import subprocess
import webbrowser
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re



def searchGoogle(textSearch, badWordsQuery):
    print("Starting Google Scholar Search")
    print '------Textsearch: {} badword: {} ---------------------\n'.format(textSearch, badWordsQuery)
    #TODO replace all spaces with % for query
    textSearch = textSearch.replace(" ", "%")
    #os.system("python scholar.py -c 30 --count 40 --phrase %s > output.txt" % textSearch)
    badword = badWordsQuery.replace(" ", "%")
    #results will have some of these words
    if badWordsQuery is '':
        print 'EMPTY bad words query: %s' % badWordsQuery
        os.system("python scholar.py -c 10 --count 10 --some %s > output.txt" % textSearch)
    else:
        print ' badWOrdsquery: %s' % badWordsQuery
        os.system("python scholar.py -c 10 --count 10 --some %s --none %s > output.txt" % (textSearch, badword))
    #cmd = "scholar.py -c 10 --phrase %s > output.txt" % textSearch
    #cmd = cmd.split()
    #subprocess.call(cmd, shell=False)

def simplifyArray(array):
    l = len(array)
    print l
    newarray = []
    print array
    for i in range(0,l):
        print '=-----------------------------------------------'
        a = array[i]
        a[0] = 0
        print a
        newarray.append(a)
    return newarray    
    
#def setupNltk():
    #dler = nltk.downloader.Downloader()
    #dler._update_index()
    #dler._status_cache['panlex_lite'] = 'installed'
    #dler.download('corpus')

#displays the URLS out of the selected objects
#returns the objects that only have URLS        
def displayUrl(array, researchObjects):
    count = 0
    documentsDisplayID = []
    
    for i in array:
        print i
        if i==1:
            #open URL
            print 'OPEN URL'
            if('URL' in researchObjects[count][0].keys()):
                print "Opening Document %d" % count
                print researchObjects[count][0]['URL']
                url = researchObjects[count][0]['URL']
                webpage = url.split()[1]
                print '----------WEBPAGE: {}'.format(webpage)
                #check for two http and remove if so
                if webpage.count("http") is 2:
                    print 'we have double http, remove first one'
                    groups = webpage.split('https')
                    print groups
                    url = 'http'+groups[1]
                    print 'GROUPS: {}    url: {}'.format(groups,url)
                    webpage = url
                
                webbrowser.open(webpage)
                documentsDisplayID.append(count)
        else:
            #Do nothing
            print "don't open Document %d" % count
        count = count + 1
    return documentsDisplayID

def removeCommonWords(documents,table):
   #remove the common words using the Natural Language ToolKit
   s = set(stopwords.words('english'))
   str1Stopped = ""
   documentlist = []
   #compile the good documents into one large string
   for i in documents:
       print i
       str2 = ''
       str1 = ''
       if('Title' in table.list[i][0].keys()):
         print table.list[i][0]['Title']
         str2 = table.list[i][0]['Title']
       if('Excerpt' in table.list[i][0].keys()):
         str1 = table.list[i][0]['Excerpt']
       str1Stopped = str1 + " " + str1Stopped + " " + str2 + " "
       #print str1Stopped
       #print table.wordListToFreqDict(str1Stopped)
       #documentlist.append(table.wordListToFreqDict(str1Stopped))
   #make strings all lower case
   str1Stopped = str1Stopped.lower()
   print str1Stopped
   #remove Excerpt and title from string
   print '-----------------remove excerpt and title from text-------'
   remove_list = ['excerpt', 'title', 'summary', '...', 'abstract']
   word_list = str1Stopped.split()
   word_list = ' '.join([i for i in word_list if i not in remove_list])
   print '-----------------word_list-------'
   print word_list
   print '-----------------common words removed-------'
   word_list = filter(lambda w: not w in s, word_list.split())
   return word_list

def commonWords(word_list):
   c = Counter(word_list)
   print c.most_common(6)
   return c.most_common(6)

def leastCommonWords(word_list):
   print '\n---------------------LEAST COMMON WORDS----------------------\n'
   c = Counter(word_list)
   length = len(word_list)
   print 'length: {}'.format(length)
   least_common = c.most_common(length)
   print least_common
   least_common = tuple(reversed(least_common))
   print '\n---------------------least_common reversed: ----------------------\n'
   print 'reversed least_common: {}'.format(least_common)
   
   #return the first 3 elements
   
   return least_common[0:1]
      
         
   #Remove the common words in documents disliked
   
   #for i in documents:
   #    print i
   #    print table.list[i][0]['Title']
   #    str1 = table.list[i][0]['Excerpt']
   #    str1Stopped = filter(lambda w: not w in s, str1.split())
   #    print str1Stopped
   #    print table.wordListToFreqDict(str1Stopped)
   #    documentlist.append(table.wordListToFreqDict(str1Stopped))
   #return documentlist

def run(textSearch, badWordsQuery):
   textSearch = textSearch.lower()
   print '\n--------------- Start of Search: {}  {}-------------------\n\n'.format(textSearch, badWordsQuery)
   searchGoogle(textSearch, badWordsQuery)
   time.sleep(1)
   print "Enter in keywords for the tfidf"
   keywords = raw_input()
   keywords = keywords.split()
   #delay 20 seconds, wait for output.txt to be generated
   print('Start tfidf')
   
   
   #create tfidf tester class
   t = TestTable()
   t.setKeywords(keywords)
   t.run()
   print '----------------------FREQUENCY -------------------------------------/n'
   print t.getFrequency()
   frequencies = t.getFrequency();
   a = simplifyArray(frequencies)
   print '----------------------FREQUENCIES -------------------------------------/n'
   print frequencies
   print '----------------------a -------------------------------------/n'
   print a
   
   kmeans2 = KmeansTest()
   kmeans2.setNpArray(a)
   checkDocs = kmeans2.calc()
   #print t.list
   
   documentDispIDs = displayUrl(checkDocs, t.list)
   documentsLiked = []
   documentsDisliked = []
   
   #Query the user to see if they like the documents
   count = 0
   total = len(documentDispIDs)
   for i in documentDispIDs:
       print 'Document ID for yes or no'
       print i
       print t.list[i]
       print t.list[i][0]['Title']
       title = t.list[i][0]['Title']
       title = title.strip()
       title = title.split()[1:]
       title = ' '.join(title)
       var = raw_input("Did you like Document %d: %s? (yes or no) " %  (i, title))
       var = var.lower()
       if var == 'yes':
           print 'User liked this Document'
           documentsLiked.append(i)
           count = count + 1
       else:
           print 'User did not like this Document'
           documentsDisliked.append(i)
   print '----------------Performance -------------------'
   print 'Recommended Document Count: %d' % total
   print 'Total documents: %d' % total
   t.performance = (float(count) / float(total)) * 100
   print 'Average Documents Liked: %f' % t.performance
   print t.performance
   
   #remove the common words using the Natural Language ToolKit
   s = set(stopwords.words('english'))
   #Remove the common words in the documents liked
   goodTextWords = removeCommonWords(documentsLiked, t)
   
   #Remove the common words in documents disliked
   badTextWords = removeCommonWords(documentsDisliked, t)
   
   print '-------------------Good Docs Cleaned-----------------------'
   print goodTextWords
   print '-------------------Good Text: Find the Most Common Words-----------------------'
   #print commonWords(goodTextWords)
   commonWords2 = commonWords(goodTextWords)
   print commonWords2
   print '-------------------Bad Text: Find the Most Common Words-----------------------'
   print commonWords(badTextWords)
   print '-------------------Bad Text: Find the Least Common Words-----------------------'
   print leastCommonWords(badTextWords)
   badWords2 = leastCommonWords(badTextWords)
   
   print '/n--------------------BAD WORDS least common-------------------------/n'
   print 'badwords2: {} '.format(badWords2)
   values = [t.performance, commonWords2, badWords2]
   return values
  
def removeNumbersFromList(mylist):
    array = []
    for x in mylist:
        print 'X: {}'.format(x)
        listNoInt = x[0]
        array.append(listNoInt)
    return array

def main(argv):
   #PERCENTAGE THRESHOLD TO EITHER ADD TO ORIGINAL QUERY OR KEEP ORIGINAL WITH NEW KEYWORDS
   #NOTE: each new search will the bad words appended to the end of their search
   performanceMetricThreshold = 70
   performanceAvg = 0.0
   searchCount = 0
   running = True
   badWordsQuery = ''
   badWords = ' '
    
    
   textSearch = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ("test.py -i <textSearch> -o <outputfile>")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("test.py -i <textSearch> -o <outputfile>")
         sys.exit()
      elif opt in ("-i", "--ifile"):
         textSearch = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Text Search is "%s"' % textSearch)
   print ('Output file is "%s"' % outputfile)
   
   while(1):
       values = run(textSearch, badWordsQuery)
       print '----------values------------'
       print values
       currentPerformance = values[0]
       commonWords = values[1]
       
       #remove numbers from badWords
       badWords = values[2]
       if badWords is not None:
           badWords = removeNumbersFromList(badWords)
       
       print '\nGOOD WORDS FROM RUN: {}'.format(commonWords)
       print '\nBAD WORDS FROM RUN: {}'.format(badWords)
       if(searchCount == 0):
           performanceAvg = currentPerformance
       else:
           performanceAvg = float(performanceAvg + currentPerformance) / 2.0 
       
       print '-----------------Performance Average: %f---------------------' % performanceAvg
       
       if(performanceAvg < performanceMetricThreshold):
           print 'Performance performanced below threshold: %d' % performanceMetricThreshold
           if commonWords is None:
               break;
           else:
            print 'COMMON WORDS: {}'.format(commonWords)
            words = commonWords
            print '-----------common words------'
            print words
            
            print 'REMOVE numbers from common list'
            words = removeNumbersFromList(words)
            print '\n----------------common words without numbers----------\n'
            print words
            textSearch = textSearch.lower()
            currentSearch = textSearch.split()
            print currentSearch
            
            
            wordFound = False
            for word in words:
                if(wordFound):
                    break;
                print word
                
                if word not in currentSearch:
                    if not wordFound:
                        textSearch = textSearch + ' ' +  word
                        wordFound = True
                    else:
                        break;
                    print '\n-----------------added word, new textSearch: %s ------------\n' % textSearch
            
           #add bad words to bad words search
           for badWord in badWords:
               badWordsQuery = badWordsQuery + ' ' + badWord
           print 'bad word query: {}'.format(badWordsQuery)        
           print '\n--------------- END OF SEARCH-------------------\n\n'
           #find most frequent word that isn't already in the title
           print 'Starting new search with %s ' % textSearch
           
       else:
           
           
           #add bad words to bad words search
           for badWord in badWords:
               badWordsQuery = badWordsQuery + ' ' + badWord
           print 'bad word query {}'.format(badWordsQuery)
           print '\n--------------- END OF SEARCH-------------------\n\n'
           var = raw_input("\nWould you like to Continue Searching? (yes or no) ")
           var = var.lower()
           if var == 'yes':
              print 'User liked this Document'
              print 'Using the same query enter in a different keyword'
              #start new search without the bad words
              
              
              #documentsLiked.append(i)
              #count = count + 1
           else:
             print 'End of Program'
             break;
       searchCount = searchCount + 1   

   #print t.wordListToFreqDict(t.list[0][0]['Excerpt'].split())


   #print [method for method in dir(t) if callable(getattr(t, method))]
   
   

if __name__ == "__main__":
   main(sys.argv[1:])
