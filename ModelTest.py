import word2vec

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import gensim
from gensim.parsing import PorterStemmer
import math
import os.path,csv,re

def cosine_similarity(vector1, vector2):
    s = 0
    v1 = 0 
    v2 = 0
  
    for p,q in zip(vector1, vector2) :
    	s = s + float(p * q)
	v1 = v1 + float(p * p)
	v2 = v2 + float(q * q)
        
 	
    den = math.sqrt(v1) * math.sqrt(v2);
    if not den:
	return 0
    return s / den
    #dot_product = sum([p*q for p,q in zip(vector1, vector2)])
    
    #magnitude = math.sqrt(sum([val**2 for val in vector1])) * math.sqrt(sum([val**2 for val in vector2]))
    #if not magnitude:
    #    return 0
    #return dot_product / magnitude


#word2vec.word2phrase('File-stemmed.txt', 'File-phrases', verbose=True)
#word2vec.word2vec('File-phrases', 'File.bin', size=100, verbose=True)
#word2vec.word2clusters('File-stemmed.txt', 'File-clusters.txt', 100, verbose=True)
###Prediction Model

model = word2vec.load('embedding_file.bin')
#wordnet_lemmatizer = WordNetLemmatizer()

#print model.vocab
#print model.vectors.shape
#print model.vectors
#print 'dog word in model '
#print model['dog'].shape
#print model['Terminal']
workingdirectory=os.getcwd()
opfile= workingdirectory + "/Dataset/test.csv"
Q = []
X = []
Y = []
with open(opfile,'rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    for row in tsvin:
        #print row[0],row[1],row[2],
        Score = row[3]
        Question = row[0]

        s = word_tokenize(Question)
        Qfeature = 0
	varQ = []
	vectorQ = []
        for i in range(50) :
    	    vectorQ.append(0)
        for x in s:
    	    try:	
    		p = unicode(x)
    	        varQ.append(p)
    	        vec = model[p]
    	        temp = [x + y for x , y in zip(vectorQ, vec)]
    	        vectorQ = temp 
            except:
    		qwer = 0
        
       
        for x in vectorQ:
	    Qfeature = Qfeature + float(x)  

        Q.append(Qfeature)

	Refans = row[1]


  	s = word_tokenize(Refans)
        var1 = []
	vector1 = []
	for i in range(50) :
    	    vector1.append(0)
        for x in s:
    	    try:	
    		p = unicode(x)
    	        var1.append(p)
    	        vec = model[p]
    	        temp = [x + y for x , y in zip(vector1, vec)]
    	        vector1 = temp 
            except:
    		print ""
	#print "First Sentence is : " + Refans
	#print "First Sentence vector : "
	#print vector1

#word = wordnet_lemmatizer.lemmatize('socks')


	Studans = row[2]
        s = word_tokenize(Studans)
        var2 = []
	vector2 = []
	for i in range(50) :
    	    vector2.append(0)

	for x in s:
            try:
    	        p = unicode(x)
    	        var2.append(p)
    	        vec = model[p]
    	        temp = [x + y for x , y in zip(vector2, vec)]
    	        vector2 = temp
            except:
	        print ""

        #print "Second Sentence is : " + Studans
        #print "Second Sentence vector : "
        #print vector2
        #print "Cosine similarity of 2 vectors is :"
 	p =  cosine_similarity(vector1 , vector2)
	X.append(p)
        #print p
	#print "Score is  : " + Score
	Y.append(Score)
	print Refans + " ---> " + Studans + " ---> " + str(p) + " ---> " + str(Score)        
	#print "-------------------------------------------------------"
#indexes1, metrics1 = model.cosine(var1)
#indexes2, metrics2 = model.cosine(var2)
#print 'Similarity of socks'
#print indexes1
#print indexes2

#print metrics1
#print metrics2
fw=open("features.csv",'w')
i=0
for i in range( len(X)):
	fw.write(str(Q[i]) + "," + str(X[i])+","+str(Y[i])+"\n")
fw.close()


