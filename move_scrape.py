#!/usr/bin/python

from urllib2 import urlopen
import re, subprocess

page = 'http://pokemondb.net/pokedex/pikachu'

url = urlopen(page)
html = url.read()

moves = re.findall(r'<a class="ent-name" href="/move/(.*?)" ',html)
moves = list(set(moves))

for a_move in moves:
	print a_move
