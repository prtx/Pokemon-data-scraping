#!/urs/bin/python

import urllib2, re, time, subprocess
from urllib2 import urlopen

try:
	page = 'http://pokemondb.net/pokedex/national'
	html = urllib2.urlopen(page).read()
	pokemons = re.findall(r'href=\"\/pokedex\/(.*?)\"><\/a><br><small>#(.*?)<\/small>',html)
	pokedex = []
	for pokemon in pokemons:
		pokedex.append([pokemon[1],pokemon[0]])	
	
	a_file = open('pokedex','w')
	for pokemon in pokedex:
		a_file.write(pokemon[0]+' '+pokemon[1]+'\n')
	a_file.close()
	print 'DONE!!!!'

except Exception, msg:
	print str(msg)

execfile('image_scrape.py')
