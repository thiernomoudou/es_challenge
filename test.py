import unittest

from pig_latin import translate


class TestPigLatin(unittest.TestCase):

    def test_word_starts_with_consonant(self):
        pig = translate('pig')
        banana = translate('banana')

        self.assertEqual(pig, 'igpay')
        self.assertEqual(banana, 'ananabay')

    def test_word_begins_with_consonnant_cluster(self):
        smile = translate('smile')
        glove = translate('glove')
        my = translate('string')
        self.assertEqual(smile, 'ilesmay')
        self.assertEqual(glove, 'oveglay')
        self.assertEqual(my, 'ingstray')

    def test_word_begins_with_voye(self):
        eat = translate('eat')
        omelet = translate('omelet')
        self.assertEqual(eat, 'eatay')
        self.assertEqual(omelet, 'omeletay')
  
    def test_full_sentence(self):
        result = translate('Hello, my name is Alice.')
        self.assertEqual(result, 'Ellohay, ymay amenay isay Aliceay.')
    
    def test_non_string_input(self):
        result = translate(392837263)
        self.assertEqual(result, 'The phrase to translate should be a string')


if __name__ == '__main__':
    unittest.main()
