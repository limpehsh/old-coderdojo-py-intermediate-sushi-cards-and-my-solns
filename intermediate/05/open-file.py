#!/usr/bin/env python

# Create a variable that holds the file.
# The "r" means you will read from the file
# You would use a "w" to write to it
# Setting the encoding to utf-8 as opposed to the default (ASCII)
# allows you to read non-ASCII
file = open("python-example.txt", "r", encoding="utf-8")
file_text = file.read()
print(file_text)

# remeber to close the file
file.close()