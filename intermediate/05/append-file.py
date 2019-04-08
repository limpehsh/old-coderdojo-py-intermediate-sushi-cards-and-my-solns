#!/usr/bin/env python

# elemantary example on appending text to a file
file = open("output-example.txt", "a")
# Note that the text starts with "\n".
# This makes sure that what you're appending starts on a new line.
# It's as though you hit the enter key wherever that appears in the text.
file.write("\nHello everyone. Now I can write to files!")

# remeber to close the file
file.close()