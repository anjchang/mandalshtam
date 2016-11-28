import glob
import re
import nltk

from nltk.corpus import stopwords

#look in source directory
glob.glob("source/*.txt")
file_list = glob.glob("source/*.txt")
print file_list

def clean(text):
    words = re.findall('[A-Za-z]+',text)  #remove punctuations
    words = list(set(words))  #remove duplicate 
    # remove all stopwords and uppercase words that are stopwords
    words = [w for w in words if not w.lower() in stopwords.words('english')]
    return words
    
#get text from files
useful_words = []
for filename in file_list:
    source = open(filename)
    text = source.read()
    useful_words += clean(text)

#sort the words in alphabetica order
useful_words.sort()
print str(len(useful_words)) + " useful words"

#use textblob classifier
from textblob import TextBlob 
usefulblob =  TextBlob(" ".join(useful_words)) 

#create output file
output_file = open('classified.txt','w')
for (word,tag) in usefulblob.tags:
    print word, tag
    output_file.write('%s %s \r\n' %( word, tag))
    
output_file.close()
