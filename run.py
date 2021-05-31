#!/usr/local/bin python3

confirm = {'yes', 'y'}

while True:
	f = input("\nInput:\n=====\n")

	print("\nOutput:\n======")
	print(f.lower())
	print("\n")

	if input("Would you like to go again?").lower() not in confirm:
		break
