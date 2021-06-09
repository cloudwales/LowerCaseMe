#!/usr/local/bin python3

import pyperclip

class Helpers():

    # Converts to lower case
    def convert_to_lowercase(arg):
        return arg.lower()

    # Formats the output to print on screen
    def format_output(arg):
        print("\n\033[1;33;40mOutput:\033[0;0m")
        print(arg)
        pyperclip.copy(arg)
        print("\n\033[3;32;40mCopied to clipboard... \033[0;0m\n")

    # Copy to clipboard
    def copy_to_clipboard(arg):
        pyperclip.copy(arg)
