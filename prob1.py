#!/usr/bin/python
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
	if len(w) > 6:
		#raw_input()
		#print words
		words.insert(0,w)
	print words
