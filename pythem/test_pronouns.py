""" Unit tests for the pronoun replacement functions"""

import unittest

from .pronouns import match_cases
from .pronouns import replace_pronoun
from .pronouns import replace_pronouns


class TestMatchCases(unittest.TestCase):

    def test_lower_case(self):
        words = ['egg', 'sausage', 'and', 'bacon']

        for word in words:
            self.assertEqual(match_cases(word, word), word)

    def test_upper_case(self):
        words = ['SPAM', 'SPAM', 'LOVELY', 'SPAM']

        for word in words:
            self.assertEqual(match_cases(word, word), word)

    def test_capitalised(self):
        words = ['Arthur', 'Bedevere', 'Lancelot', 'Robin']

        for word in words:
            self.assertEqual(match_cases(word, word), word)

    def test_unknown_case_is_lowered(self):
        originals = ['sHe', 'hiM', 'hErSeLf']
        replacements = ['they', 'them', 'themselves']
        targets = ['they', 'them', 'themselves']
        for original, replacement, target in zip(originals, replacements, targets):
            self.assertEqual(match_cases(original, replacement), target)


class TestReplacePronoun(unittest.TestCase):

    def test_non_pronouns_not_affected(self):
        non_pronoun_words = "there's egg and bacon; " \
                            "egg sausage and bacon; " \
                            "egg and spam; " \
                            "egg bacon and spam; " \
                            "egg bacon sausage and spam; " \
                            "spam bacon sausage and spam; " \
                            "spam egg spam spam bacon and spam; " \
                            "spam sausage spam spam bacon spam tomato and spam"

        for word in non_pronoun_words.split():
            self.assertEqual(replace_pronoun(word), word)

    def test_neutral_pronouns_not_affected(self):
        neutral_pronouns = "they them their it its"

        for word in neutral_pronouns.split():
            self.assertEqual(replace_pronoun(word), word)

    def test_male_pronouns_replaced_simple(self):
        male_pronouns = ['he', 'him', 'his']
        replacements = ['they', 'them', 'their']

        for word, replacement in zip(male_pronouns, replacements):
            self.assertEqual(replace_pronoun(word), replacement)

    def test_female_pronouns_replaced_simple(self):
        female_pronouns = ['she', 'hers']
        replacements = ['they', 'theirs']

        for word, replacement in zip(female_pronouns, replacements):
            self.assertEqual(replace_pronoun(word), replacement)

    def test_her_replaced_by_them(self):
        """ Depending on context, 'her' should either be them or their.
            Since this will be tricky to solve, let's assume all instances
            of 'her' mean 'them' for now..."""
        self.assertEqual(replace_pronoun('her'), 'them')

    def test_his_replaced_by_their(self):
        """ Depending on context, 'his' should either be their or theirs.
            Since this will be tricky to solve, let's assume all instances
            of 'his' mean 'their' for now..."""
        self.assertEqual(replace_pronoun('his'), 'their')

    def test_gendered_pronouns_replaced_punctuation(self):
        pronouns = ['he.', 'him,', '\'his', 'she;', 'her:', '/hers',
                    'he/', 'him\"', 'his!', '\"she', '-her', '*hers',
                    'he?', '(him', '(his)', '{she', 'her}', '[hers', 'he]']

        replacements = ['they.', 'them,', '\'their', 'they;', 'them:', '/theirs',
                        'they/', 'them\"', 'their!', '\"they', '-them', '*theirs',
                        'they?', '(them', '(their)', '{they', 'them}', '[theirs', 'they]']

        for word, replacement in zip(pronouns, replacements):
            self.assertEqual(replace_pronoun(word), replacement)

    def test_gendered_pronouns_not_replaced_within_words(self):
        pronouns = ['the', 'himalayas', 'history', 'banshee;', 'herd', 'ushers']

        for word in pronouns:
            self.assertEqual(replace_pronoun(word), word)

    def test_capitalised_words_returned_correctly(self):
        words = ['She', 'Him', 'Their', 'Spam', 'Eggs']
        replacements = ['They', 'Them', 'Their', 'Spam', 'Eggs']

        for word, replacement in zip(words, replacements):
            self.assertEqual(replace_pronoun(word), replacement)


class TestReplacePronouns(unittest.TestCase):

    def test_single_word(self):
        input_text = "himself"
        output_text = "themselves"

        self.assertEqual(replace_pronouns(input_text),output_text)

    def test_multiple_words(self):
        input_text = "Why can't she have egg bacon spam and sausage?"
        output_text = "Why can't they have egg bacon spam and sausage?"

        self.assertEqual(replace_pronouns(input_text), output_text)

    def test_multiple_spaces_between_words_removed(self):
        """ This would be a bit of a pain to keep track of otherwise"""
        input_text = "Why  can't  she  have  egg  bacon  spam  and  sausage?"
        output_text = "Why can't they have egg bacon spam and sausage?"

        self.assertEqual(replace_pronouns(input_text), output_text)