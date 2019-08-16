import unittest
from module import search_deplicated , judge_anagram


class TestSearchDeplicated(unittest.TestCase):
    '''
    search_deplicatedモジュールのテストをするクラス
    '''

    def test_search_deplicated(self):
        '''
        search_deplicatedのテストを行う
        '''

        list = ["アンパンマン" , "ばいきんまん" , "ジャムおじさん"]
        expect = [False , False , True]
        for idx , value in enumerate(list):
            result = search_deplicated.search_deplicated(value)
            self.assertEqual(result , expect[idx])

    def test_judge_anagram(self):
        '''
        judge_anagramのテストを行う
        '''

        list = [["hoge","geho"],["abcd","abc"],["aaas","aaas "]]
        expect = [True , False, False]
        for idx , value in enumerate(list):
            result = judge_anagram.judge_anagram(value[0],value[1])
            self.assertEqual(result , expect[idx])

    def testURLify(self):
        '''
        URLifyのテストを行う
        :return:
        '''

if __name__ == "__main__":
    unittest.main(verbosity=2)



