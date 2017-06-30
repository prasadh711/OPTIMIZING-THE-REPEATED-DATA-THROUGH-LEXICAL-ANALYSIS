#!/usr/bin/env python
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re 
import tkinter
import sys
import os
import re, math
from collections import Counter

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def getsentences(str):
	str = re.sub('\.','. ',str)
	str = re.sub('\?','? ',str)	
	return str

def gettokens(Sentence):
	tokens = []
	for sentence in Sentence: 
		print(sentence)
		tokens.append(word_tokenize(sentence))
	return tokens

def main():
	Sentences = []	
	myfile = open(str(entry1.get()),"r") 
	data = myfile.read()
	data = data.lower();
	data = getsentences(data)
	Sentences = sent_tokenize(data)
	#print(Sentences)	
	tokens = word_tokenize(data)
	#print(tokens)
	newsentence=""
	finalsentences = []
	finalsentences.append(Sentences[0])
	newsentence=newsentence+Sentences[0]	
	flag=0
	i=-1
	for sentence in Sentences:
		flag=0		
		i=i+1
		if(i==1):
			text1=Sentences[0]
			text2=Sentences[1]
			vector1 = text_to_vector(text1)
			vector2 = text_to_vector(text2)
			cosine = get_cosine(vector1, vector2)
			if(cosine < 0.60):
				finalsentences.append(Sentences[1])
				newsentence=newsentence+Sentences[1]	
			continue
		for index in range(i-1):
			text1 = sentence
			text2 = Sentences[index]
			vector1 = text_to_vector(text1)
			vector2 = text_to_vector(text2)
			cosine = get_cosine(vector1, vector2)
			if(cosine > 0.60):
				flag=1
		if(flag == 0 and i>1):
			finalsentences.append(sentence)
			newsentence=newsentence+sentence				
	print(finalsentences)		
	print(newsentence)
    	token.insert(tkinter.INSERT, tokens)
	answer.insert(tkinter.INSERT,newsentence)

root=tkinter.Tk()
root.title("Optimizing the unwanted/repeated data through lexical analysis")
root.geometry("1000x1000")
upframe=tkinter.Frame(root,height=200,width=200)
upframe.pack()
downframe=tkinter.Frame(root,height=200,width=200)
downframe.pack()
label1=tkinter.Label(upframe,text="Enter the Directory Path")
label1.pack()
entry1=tkinter.Entry(upframe,width=500)
entry1.pack(fill=tkinter.X)
button1=tkinter.Button(upframe,text="Scan",command=main)
button1.pack()
label2=tkinter.Label(upframe,text="Tokens")
label2.pack()
token=tkinter.Text(downframe,width=500)
token.pack()
label3=tkinter.Label(downframe,text="Optimized Sentences")
label3.pack()
answer=tkinter.Text(downframe,width=500)
answer.pack()
root.mainloop()
#text1 = 'This sentence is similar to a foo bar sentence .ajeya is my name.india is my country'
#text2 = 'This sentence is similar to a foo bar sentence .'

#vector1 = text_to_vector(text1)
#vector2 = text_to_vector(text2)

#cosine = get_cosine(vector1, vector2)

#print 'Cosine:', cosine