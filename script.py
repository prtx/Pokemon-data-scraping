#!/urs/bin/python

import urllib2, re, time, subprocess
from urllib2 import urlopen
import sqlite3

db = sqlite3.connect('Pokedex.db')
dex = db.cursor()

db.execute('create table Poke_Name (ID int primary key, Name text)')
db.execute('create table Poke_Name (ID int primary key, Name text)')


#try:
	
page = 'http://pokemondb.net/pokedex/national'
html = urllib2.urlopen(page).read()
print 'Read!!!'
pokemons = re.findall(r'href=\"\/pokedex\/(.*?)\"><\/a><br><small>#(.*?)<\/small>',html)

pokedex = []
for name,ID in pokemons:
	print (ID,name)

	page = 'http://pokemondb.net/pokedex/'+name
	html = urllib2.urlopen(page).read()
	
	base_stat = re.findall(r'Base stats.*?<b>([0-9]*?)</b>',html,re.DOTALL)
	base_exp = re.findall(r'Base EXP.*?<td>([0-9]*?)</td>',html,re.DOTALL)

	poke_type = re.findall(r'<a href="/type/(.*?)".*?introduced in',html)
	move_list = re.findall(r'<td class="num">([0-9].?)</td>.*?href="/move/(.*?)".*?href="/type/(.*?)".*?<td class="num">([0-9]*?)</td> <td class="num"\s>([0-9]*?)</td>',html[:html.find('Egg moves')])

	
	pokedex.append((ID,name))	
	db.execute('insert into Poke_Name values(?,?)',(int(ID),name))
print 'DONE!!!!'




#except Exception, msg:
#	print str(msg)

db.commit()
db.close()

base_stat = re.findall(r'Base stats.*?<b>([0-9]*?)</b>',html,re.DOTALL)
base_exp = re.findall(r'Base EXP.*?<td>([0-9]*?)</td>',html,re.DOTALL)


#({[IV+2*Base Stat+([EVs]/4)+100] * Level}/100)+10
