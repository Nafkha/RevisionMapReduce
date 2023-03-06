#!/usr/bin/python3

import sys

current_cat = None
total_vente = 0
cat = None


for line in sys.stdin:
	line = line.strip()
	cat, vente = line.split('\t')
	try:
		vente = float(vente)
	except ValueError:
		continue
	if current_cat == cat:
		total_vente += vente
	else:
		if current_cat:
			print(current_cat,'\t',total_vente)
		total_vente = vente
		current_cat = cat
if current_cat == cat:
	print(current_cat,'\t',total_vente)
