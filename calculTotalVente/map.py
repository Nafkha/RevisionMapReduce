#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	if len(line)==0:
		continue
	words = line.split()
	print(words[2],'\t',words[-1])
