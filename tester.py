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


def searchGoogle(textSearch):
    print("Starting Google Scholar Search")
    #TODO replace all spaces with % for query
    textSearch = textSearch.replace(" ", "%")
    os.system("python scholar.py -c 10 --phrase %s > output.txt" % textSearch)
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
                webbrowser.open(webpage)
                documentsDisplayID.append(count)
        else:
            #Do nothing
            print "don't open Document %d" % count
        count = count + 1
    return documentsDisplayID


def main(argv):
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
   
       
   
   searchGoogle(textSearch)
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
           count = count + 1
       else:
           print 'User did not like this Document'
   print '----------------Performance -------------------'
   print 'Recommended Document Count: %d' % total
   print 'Total documents: %d' % total
   t.performance = (float(count) / float(total)) * 100
   print 'Average Documents Liked: %f' % t.performance
   print t.performance


   #print [method for method in dir(t) if callable(getattr(t, method))]
   
   

if __name__ == "__main__":
   main(sys.argv[1:])
