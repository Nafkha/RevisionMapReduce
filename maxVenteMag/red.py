#!/usr/bin/python3

import sys

current_shop = None
max_vente  = 0
shop = None

for line in sys.stdin:
	line = line.strip()
	shop, vente = line.split('\t')
	
	try:
		vente = float(vente)
	except ValueError:
		continue
	if shop == current_shop:
		if vente>=max_vente:
			max_vente = vente
	else:
		if current_shop:
			print(current_shop,'\t',max_vente)
		current_shop = shop
		max_vente = vente
if current_shop == shop:
	print(current_shop,'\t',max_vente)
