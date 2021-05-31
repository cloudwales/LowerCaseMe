#!/usr/local/bin python3
import pyperclip

def lowercase(sentence):
    pyperclip.copy(sentence.lower())
    print("\n\033[1;33;40mOutput:\033[0;0m")
    print(sentence.lower())
    pyperclip.copy(sentence.lower())
    print("\n\033[3;32;40mCopied to clipboard... \033[0;0m\n")

while True:
	sentence = input("\n\033[1;33;40mInput:\033[0;0m\n")
	lowercase(sentence)

	if input("Would you like to convert another sentance? ").lower() not in ('y', 'yes'):
		break
