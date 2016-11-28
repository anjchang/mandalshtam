#python 2.7 
import glob
import re
import nltk
from textblob import TextBlob 

from nltk.corpus import stopwords

glob.glob("source/*.txt")
file_list = glob.glob("source/*.txt")
print "processing "
print file_list
print '\r\n'

def classify(source):  #create TextBlob object from source
    blob = TextBlob(source)
    return blob

def cleanblob(sourceblob): #clean the text and return wordlist
    print sourceblob
    print '\r\n'
    sourcewords =  str(sourceblob.words)
    words = re.findall('[A-Za-z]+',sourcewords)  #remove punctuations
    words = list(set(words))  #remove duplicate 
    # remove all stopwords and uppercase words that are stopwords
    words = [w for w in words if not w.lower() in stopwords.words('english')]
    words.sort()
    return words 


useful_words = []
for filename in file_list:
    source = open(filename)
    text = source.read()
    text = text.decode('ascii', errors="ignore") #get rid of unicode errors for extblob    
    sourceblob = classify(text) #classify poems
    words = cleanblob(sourceblob) #get keywords 
    output_file = open('output.txt','w')
    for keyword in words:
        for (word,tag) in sourceblob.tags:
            if keyword == word:
                print word,tag
                output_file.write('%s %s\r\n' %( word, tag))
    output_file.close
    
print "done, look in output.txt"
