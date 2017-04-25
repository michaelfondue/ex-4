#!/usr/bin/env python3
# coding: utf-8

# 
# Uebung 4, Aufgabe 1
# Michael Balmer, 12-923-363

import io
import sys
import xml.etree.ElementTree as ET
import json
import glob
from lxml import etree

def getfreqwords(indir, outfile):
	
	sacbooks = []
	sacbooks = glob.glob(indir + 'SAC-Jahrbuch_*.xml', recursive=False)
	
	for file in sacbooks:
		#with open(file) as src, open('output.txt', 'w') as trg:
		sentences = []
		tree = etree.parse(file)
		sentences.append(file.get('s')
			
			#sentence_hashes = set()
			#for sentence in src:
				#sentence_hash = hash(sentence)
				#if sentence_hash not in sentence_hashes:
				#	sentence_hashes.add(sentence_hash)
				#	trg.write(sentence)

	outputfile = open(outfile , 'w')
	for x in sacbooks:
		outputfile.write(x)

	outputfile.close()



def main():

	getfreqwords('SAC/', 'output.txt')	



if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()