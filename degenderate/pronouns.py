""" Functions for finding and replacing pronouns etc in strings"""

import re

# Just a small table for development
pronoun_replacements = {
    'he': 'they',
    'him': 'them',
    'his': 'their',
    'himself': 'themselves',
    'she': 'they',
    'her': 'them',
    'hers': 'theirs',
    'herself': 'themselves'
}


def match_cases(original, replacement):
    """ Returns a copy of the replacement word with the cases
        altered to match the original word's case
        Only supports upper case, capitalised (title) and lower case -
        everything else gets lower cased by default"""
    if original.isupper():
        return replacement.upper()
    if original.istitle():
        return replacement.title()
    return replacement


def replace_pronoun(input_word):
    """ Check a single word to see if it's gendered; if it is then replace it"""
    # Remove all whitespace before we check for pronoun status
    cleaned_word = re.sub(r'[^\w\s]','', input_word)
    cleaned_word_lower = cleaned_word.lower()

    if cleaned_word_lower in pronoun_replacements:
        replacement = match_cases(cleaned_word, pronoun_replacements.get(cleaned_word_lower))
        return input_word.replace(cleaned_word, replacement)
    return input_word

def replace_pronouns(input_string):
    """ Return a copy of the input string with all of the gendered pronouns replaced"""
    return ' '.join(replace_pronoun(word) for word in input_string.split())