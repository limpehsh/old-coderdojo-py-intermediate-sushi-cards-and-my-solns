#!/usr/bin/env python

# example on writing out to a file
output_filename = "output-example.txt"
file = open(output_filename, "w", encoding="utf-8")
file.write("Hello everyone. Now I can write to files!")
non_ascii_example = "春ねむり"
file.write("\n")
file.write(non_ascii_example)

# remeber to close the file
file.close()