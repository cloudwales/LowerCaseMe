#!/usr/local/bin python3

import pyperclip

class Helper():

    def convert_to_lowercase(sentence):
        pyperclip.copy(sentence.lower())
        print("\n\033[1;33;40mOutput:\033[0;0m")
        print(sentence.lower())
        pyperclip.copy(sentence.lower())
        print("\n\033[3;32;40mCopied to clipboard... \033[0;0m\n")
