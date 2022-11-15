import unittest
import cap

class TestCap(unittest.TestCase):
    def setUp(self):
        "在每个测试方法执行之前执行"
        pass

    def tearDown(self):
        "在每个测试方法执行之后执行"
        pass

    def test_None(self):
        text = None
        result = cap.just_do_it(text)
        self.assertEqual(result, None)

    def test_one_word(self):
        text = 'duck'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')

    def test_words_with_apostrophes(self):
        text = "I'm fresh out of ideas"
        result = cap.just_do_it(text)
        self.assertEqual(result, "I'm Fresh Out Of Ideas")
    
    def test_words_with_quotes(self):
        text = "\"You're despicable,\" said Daffy Duck"
        result = cap.just_do_it(text)
        self.assertEqual(result, "\"You're Despicable,\" Said Daffy Duck")

    def test_words_with_more_upper(self):
        text = "\"You're desPICable,\" said Daffy Duck"
        result = cap.just_do_it(text)
        self.assertEqual(result, "\"You're Despicable,\" Said Daffy Duck")

if __name__ == '__main__':
    unittest.main()