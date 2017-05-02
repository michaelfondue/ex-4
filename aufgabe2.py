#!/usr/bin/env python3
# coding: utf-8

# 
# Uebung 4, Aufgabe 2
# Michael Balmer, 12-923-363

import io
import sys
import json
import glob
import string
import random
import urllib.request
import bz2
from lxml import etree as ET



def gettitles(infile, testfile, trainfile, k):
	
	testoutputfile = open(testfile , 'w', encoding = 'utf-8')
	trainoutputfile = open(trainfile , 'w', encoding = 'utf-8')

	path = infile
	with BZ2File(path) as xml_file:
    	parser = et.iterparse(xml_file, events=('end'))
    	for events, elem in parser:
        	if elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}title":
            	testoutputfile.write(sample(path, 20))
        	else:
        		trainoutputfile.write(elem.tag)
            	
	testoutputfile.close()
	trainoutputfile.close()


def sample(iterable, k):

	reservoir = []
	for t, item in enumerate(iterable):
		if t < k:
			reservoir.append(item)
		else:
			m = random.randint(0,t)
			if m < k:
				reservoir[m] = item
	return reservoir


	



def main():

	urldata = urllib.request.urlopen('https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2')
	bla = urldata.read()
	print(bla)
	data = bz2.open(urldata)

	gettitles('data', 'test.txt', 'train.txt', 20)	



if __name__ == '__main__':
    main()