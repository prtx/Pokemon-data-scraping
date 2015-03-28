#!/uar/bin/python

import re, subprocess

a_file = open('pokedex')
data = a_file.read()
a_file.close()
pokemons = re.findall(r'(.*?)\s(.*?)\n',data)


not_retrieved = []

for pokemon in pokemons:
	try:
		print pokemon
		subprocess.check_output(['wget http://img.pokemondb.net/artwork/'+pokemon[1]+'.jpg'],shell=True)
		subprocess.check_output(['mv '+pokemon[1]+'.jpg '+pokemon[0]+'_'+pokemon[1]+'.jpg'],shell=True)
	except Exception:
		not_retrieved.append(pokemon)

print not_retrieved
