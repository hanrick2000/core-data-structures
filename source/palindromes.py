#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here

    #if text is empty, return True #base case
    if text.lower() == "":
        return True
    if len(text) == 1:
        return True
  

    #clean text for analyzing
    new_text = text.replace(',', '').replace('!', '').replace('.', '').replace(' ', '').replace('-', '').replace('?', '').replace('\'', '').lower()
    
    
    #reverse splices original text into new array
    back_text = new_text[::-1]
  
    
    #creating index counter for text indices
    index = 0

    #while index in the range of the text length
    while index < len(new_text):
        #if each string has the same character as the same index
        if new_text[index] == back_text[index]:
            #check the next character
            index += 1
        #if we get through all of the characters, it is a palindrome
        elif new_text[index] != back_text[index]:
            return False

    return True
    

    #once implemented, change is_palindrome to call is_palindrome_iterative
    #to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
