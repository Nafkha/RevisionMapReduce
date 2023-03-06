#!/usr/bin/python3

import sys

current_shop = None
vente_count = 0
boutique = None
for line in sys.stdin:
	line = line.strip()
	boutique, vente = line.split('\t')
	try:
		vente = float(vente)
	except ValueError:
		continue
	if current_shop == boutique:
		vente_count += vente
	else:
		if current_shop:
			print(current_shop,'\t',vente_count)
		current_shop = boutique
		vente_count = vente
if current_shop == boutique:
	print(current_shop,'\t',vente_count)
