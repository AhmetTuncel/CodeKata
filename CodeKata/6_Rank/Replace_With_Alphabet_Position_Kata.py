"""
Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. a being 1, b being 2, etc. As an example:
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):

        text = text.lower()
        result = ''
        for i in text:
            if i.isalpha() == True:
                result = result + ' ' + str(alphabet.index(i) + 1)
        return result.lstrip(' ')

