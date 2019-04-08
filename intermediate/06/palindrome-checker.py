#!/usr/bin/env python

# Function returns a boolean depending on the input being a palindrome or not
def is_palindrome(txt):
  # make all chars the same casing, lowercase here
  lower_txt = txt.lower()

  # only keep alphabetic chars
  alphabet_only = get_alphabets_only(lower_txt)
  
  # convert string to list
  char_list = list(alphabet_only)

  # reverse the list
  reversed_char_list = get_reversed_list(char_list)

  # check if the line is a palindrome or not
  answer = True if (char_list == reversed_char_list) else False
  return answer


# Function retuns the parsed string without non-alphabet chars
def get_alphabets_only(str_obj):

  # regular expressions library
  import re
  # regex to only allow alphabet chars
  regex = re.compile("[^a-zA-Z]")
  alphabet_only = regex.sub("", str_obj)

  return alphabet_only


# Function returns a reversed list
def get_reversed_list(list_obj):
  reversed_list = list(list_obj)
  reversed_list.reverse()
  # or reversed_list = list_obj[::-1]
  return reversed_list


# settings for output files
output_filename_palindromes = "palindromes.txt"
output_filename_not_palindromes = "not-palindromes.txt"
out_true = open(output_filename_palindromes, "a")
out_false = open(output_filename_not_palindromes, "a")

# settings for input file
input_filename = "py-pal.txt"
input_file = open(input_filename, "r")

# split the file into lines
file_lines = input_file.readlines()

zero_palindromes = True
# commence the checker
print("Running Palindrome Checker...\n")
# Get rid of new line instructions for each line
for num, line in enumerate(file_lines, 1):
  if (is_palindrome(line.rstrip("\r\n"))):
    zero_palindromes = False
    out_true.write(line)
    print("palindrome found at line", num, "-", line.rstrip("\r\n"))
  else:
    out_false.write(line)
if (zero_palindromes == False):
  print("\n")
print("Palindrome Checker is completed. Please check your output files.")

# close the files
input_file.close()
out_true.close()
out_false.close()