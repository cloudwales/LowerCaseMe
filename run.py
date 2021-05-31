#!/usr/local/bin python3

confirm = {'yes', 'y'}

def lowercase(sentence):
    print("\nOutput:\n======")
    print(sentence.lower())
    print("\n")


while True:
	sentence = input("\nInput:\n=====\n")
	lowercase(sentence)

	if input("Would you like to convert another sentance?").lower() not in confirm:
		break
