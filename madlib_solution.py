"""
python 3.7.4
madlib.py

Program Description: This program will contain at least 10 variables that will be printed within a short paragraph to be a complete Mad Lib.
Input:  A short paragraph with blanks
        At least 10 variables that will store 3 different data types (string, integer, and boolean).
        [Optional] A variable that stores the madlib.
Output: Print out a madlib that uses the variables as the blanks within a madlib
        [Optional] Figure out how to use the string.format() function to fill out a madlib variable without changing data types.
"""
# Write a short story and omit words using {}
madlib = "My name is {} and I grew up in {}. I was {} when I {} out that what my {} told me about {} was {}. I have told {} of my {} friends and now we must {} tell others."

# Create, name, and assign variables that will replace the {}
proper_noun = "Lance"
location = "Paris"
age = 10
verb_past_tense = "drank"
family_member = "uncle"
mythical_creature = "mermaids"
true_or_false = True
number = 7
adjective = "worst"
adverb = "quickly"

'''
print the madlib concatenated with the variables.
record the type of error and a short description of what is raised the error with an in-line comment.
record what changes were made between iterations with an in-line comment
use in-line comments to retain but not run the print function that raise the error
record the output of the print functions that doesn't raise any errors with an in-line comment
'''

#print("My name is "+proper_noun+" and I grew up in "+location+". I was "+age+" when I "+verb_past_tense+" out that what my "+family_member+" told me about "+mythical_creature+" was "+true_or_false+". I have told "+number+" of my "+adjective+" friends and now we must "+adverb+" tell others.")
#Output & Error: TypeError: only concatenates strings not integers
#Changes: Use str() on the 2 variables that are integers 'age' and 'number' to change datat type for printing.

#print("My name is "+proper_noun+" and I grew up in "+location+". I was "+str(age)+" when I "+verb_past_tense+" out that what my "+family_member+" told me about "+mythical_creature+" was "+true_or_false+". I have told "+str(number)+" of my "+adjective+" friends and now we must "+adverb+" tell others.")
#Output & Error: TypeError: only concatenates strings not boolean
#Changes: Use str() on the 1 variable that is a boolean 'true_or_false' to change data type for printing.

print("My name is "+proper_noun+" and I grew up in "+location+". I was "+str(age)+" when I "+verb_past_tense+" out that what my "+family_member+" told me about "+mythical_creature+" was "+str(true_or_false)+". I have told "+str(number)+" of my "+adjective+" friends and now we must "+adverb+" tell others.")
#Output: My name is Lance and I grew up in Paris. I was 10 when I drank out that what my uncle told me about mermaids was True. I have told 7 of my worst friends and now we must quickly tell others.

''' Optional: Discover how to use the string.format() function to fill out a madlib variable without changing data types.'''
print(madlib.format(proper_noun, location, age, verb_past_tense, family_member, mythical_creature, true_or_false, number, adjective, adverb))
#output: My name is Lance and I grew up in Paris. I was 10 when I drank out that what my uncle told me about mermaids was True. I have told 7 of my worst friends and now we must quickly tell others.

''' Optional: add another data type and describe what it is'''
age_exact = 10.4 # this is a float data type. it contains a number with a decimal place.  
print(type(age_exact))
#output: <class 'float'>
madlib_new = "My name is {} and I grew up in {}. I was {} years old when I {} out that what my {} told me about {} was {}. I have told {} of my {} friends and now we must {} tell others."
print(madlib_new.format(proper_noun, location, age_exact, verb_past_tense, family_member, mythical_creature, true_or_false, number, adjective, adverb))
#output: My name is Lance and I grew up in Paris. I was 10.4 years old when I drank out that what my uncle told me about mermaids was True. I have told 7 of my worst friends and now we must quickly tell others.

'''Optional: Add a new line between each new sentence.'''
madlib_newline = "My name is {} and I grew up in {}. \nI was {} when I {} out that what my {} told me about {} was {}.\nI have told {} of my {} friends and now we must {} tell others."
# the way to print out a newline is by including \n into the string. 
print(madlib_newline.format(proper_noun, location, age, verb_past_tense, family_member, mythical_creature, true_or_false, number, adjective, adverb))
#output:    My name is Lance and I grew up in Paris.
#           I was 10 when I drank out that what my uncle told me about mermaids was True.
#           I have told 7 of my worst friends and now we must quickly tell others.
