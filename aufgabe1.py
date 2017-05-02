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
	sent = set()

	sacbooks = glob.glob(indir + 'SAC-Jahrbuch_*.xml', recursive=False)
	#print(sacbooks)
	outputfile = open(outfile , 'w', encoding = 'utf-8')
	#test = open(sacbooks[0], 'r')
	#print(test.read())
	#test.close()
	for sacbook in sacbooks:
		tree = ET.parse(sacbook)
		root = tree.getroot()
		for sentence in root.findall('.//s'):
			#element.append(ET.tostring(sentence, method = 'text', pretty_print = True, encoding='utf-8'))
			sente = ET.tostring(sentence, method = 'text', pretty_print = True, encoding ='utf-8')
			sentstr = str(sente, 'utf-8').split()
			if (len(sentstr) >= 6):
				for x in string.punctuation:
					if x in sentstr:
						sentstr.remove(x)
				sentforhash = ' '.join(sentstr)
				sent_hash = hash(sentforhash)
				if sent_hash not in sent:
					sent.add(sent_hash)
					outputfile.write(sentforhash + '\n')

		# 	sent.add(x)

	outputfile.close()
		#print(ET.tostring(sentence, method = 'text', pretty_print = True, encoding='utf-8'))
	 	#print('nächster Satz')
		

		# for word in element:
		# 	strword = str(word, 'utf-8')
		# 	words.append(strword.split())
	 	

	 		#print(ET.tostring(word, method = 'text', encoding='utf-8'))
	
	#if (len(sent) >= 6):
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