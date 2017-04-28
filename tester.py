from bs4 import BeautifulSoup
import scholar
import sys, getopt, os
from pdf2text import convert_pdf_to_txt
from tfidf import tfidf
from TestTfIDF import TestTable
import time


def searchGoogle(textSearch):
    print("Starting Google Scholar Search")
    #TODO replace all spaces with % for query
    textSearch = textSearch.replace(" ", "%")
    os.system("scholar.py -c 2 --phrase %s > output.txt" % textSearch)

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
   time.sleep(2)
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
   #f = open("output.txt", 'w')
   #keywords = ['government', 'USA','combat', 'Flying']
   #tfidfTest2.calc(keywords)
   #t.run()
   #print t.table
   print [method for method in dir(t) if callable(getattr(t, method))]
   
   

if __name__ == "__main__":
   main(sys.argv[1:])
