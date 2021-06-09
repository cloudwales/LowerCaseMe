#!/usr/local/bin python3

from Helpers import *


while True:
    sentence_input = input("\n\033[1;33;40mInput:\033[0;0m\n")
    converted_sentence = Helpers.convert_to_lowercase(sentence_input)
    Helpers.format_output(converted_sentence)
    Helpers.copy_to_clipboard(converted_sentence)

    if input("Would you like to convert another sentance? [y]yes or [n]no \n").lower() not in ('y', 'yes'):
        break
