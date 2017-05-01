#!/usr/bin/env python3
# coding: utf-8

# 
# Uebung 4, Aufgabe 1
# Michael Balmer, 12-923-363

import io
import sys
import json
import glob
import string

#from lxml import etree as ET
from lxml import etree as ET

def getfreqwords(indir, outfile):
	sentences_count = {}
	sacbooks = []
	element = []
	words = []
	sent = []
	
	sacbooks = glob.glob(indir + 'SAC-Jahrbuch_*.xml', recursive=False)
	#print(sacbooks)
	#test = open(sacbooks[0], 'r')
	#print(test.read())
	#test.close()
	tree = ET.parse(sacbooks[0])
	root = tree.getroot()
	for sentence in root.findall('.//s'):
		element.append(ET.tostring(sentence, method = 'text', pretty_print = True, encoding='utf-8'))

		#print(ET.tostring(sentence, method = 'text', pretty_print = True, encoding='utf-8'))
	 	#print('nächster Satz')
		for word in element:
			strword = str(word, 'utf-8')
			words.append(strword.split())
	 		#print(ET.tostring(word, method = 'text', encoding='utf-8'))
	
	for sent in words:
		for x in string.punctuation:
			if (x in sent):
				sent.remove(x)
		if (len(sent) >= 6):
			print(set(sent))
	#print(words)
	#print(element[0])
	#print(ET.tostring(sentencelist[0]))
	#print(ET.tostring(root, pretty_print=True))

	# for file in sacbooks:
	# 	#with open(file) as src, open('output.'txt', 'w') as trg:
	# 	sentence_hash = set()
	# 	tree = ET.parse(sacbooks[0])
	# 	root = tree.getroot()
	# 	print(root.get('lemma'))

	# 	for word in root:
			#print(ET.tostring(word, encoding='utf8', method='xml'))
		#print(tree.findall('<s*>'))
	#	sentences.append(hash(tree.findall('<s*<\\s>')))
		#sentence_hash.append(tree.findall('<s*<\\s>'))
		#print(sentences[0])


	# for words in sentence_hash:
	# 	#if(len(words.split()) >= 6):
	# 	if(words in sentences_count):
	# 		num = sentences_count[words]
	# 		sentences_counts[words] = num + 1
	# 	else:
	# 		sentences_count.update({words:1})
	# list = sorted(sentences_count.items())
	# for x in range(0,20):
	# 	print(sentenced_count[x])
		



			#sentence_hashes = set()
			#for sentence in src:
				#sentence_hash = hash(sentence)
				#if sentence_hash not in sentence_hashes:
				#	sentence_hashes.add(sentence_hash)
				#	trg.write(sentence)

	#outputfile = open(outfile , 'w')
	#for x in sacbooks:
	#	outputfile.write(x)

	#outputfile.close()



def main():

	getfreqwords('SAC/', 'output.txt')	



if __name__ == '__main__':
    main()