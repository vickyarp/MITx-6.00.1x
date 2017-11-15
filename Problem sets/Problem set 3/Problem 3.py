#Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, 
#lettersGuessed. This function returns a string that is comprised of lowercase English letters - 
#all lowercase English letters that are not in lettersGuessed.
#
#Example Usage:
#
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz
#Note that this function should return the letters in alphabetical order, as in the example above.
#
#For this function, you may assume that all the letters in lettersGuessed are lowercase.
#
#Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s=string.ascii_lowercase
    for char in lettersGuessed:
        s=s.replace(char,'')
    return s
     
import string