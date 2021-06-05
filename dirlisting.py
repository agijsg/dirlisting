#!/usr/bin/env python

# @author : agijsg 
# @date : 14/04/2021

# @utility : This program will list every directory of a website if the directory is specified
#			 in the dictionnary

# @usage : dirlisting.py https://website.com <directory_listing_dictionnary.txt>

import sys
import urllib

def dirlisting(website,dictionnary):
	print('\nDirectory Listing for website : '+ website + ' with the dictionnary : ' + dictionnary+'\n')
	
	dictionnary = open(dictionnary,'r').read().split('\n')
	print("File imported and read !")
	
	website_status = urllib.urlopen(website).code
	if not website_status < 500 :
		print('Website index response code : '+ str(website_status) )
		print('Website not reachable ...')
		print('Exiting program ...')
		exit(0)

	for endpoint in dictionnary:
		url = urllib.urlopen(website+'/'+endpoint)
		print('Trying with the following endpoint : '+endpoint)
		if url.code == 200:
			print('\t\t'+ website+'/'+endpoint)

if __name__=='__main__':
	dirlisting(sys.argv[1],sys.argv[2])
