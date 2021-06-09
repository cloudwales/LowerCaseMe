#!/usr/local/bin python3

from Helper import *

while True:
	sentence = input("\n\033[1;33;40mInput:\033[0;0m\n")

	Helper.convert_to_lowercase(sentence)

	if input("Would you like to convert another sentance? [y]yes or [n]no \n").lower() not in ('y', 'yes'):
		break
