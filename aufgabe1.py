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
	print(sacbooks)


	outputfile = open(outfile , 'w')
	for x in sacbooks:
		outputfile.write(x)

	outputfile.close()



def main():

	getfreqwords('x', 'bla.txt')	



if __name__ == '__main__':
    main()