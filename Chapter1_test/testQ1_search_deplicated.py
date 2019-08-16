import unittest
from Chapter1 import search_deplicated

class TestSearchDeplicated(unittest.TestCase):
    '''
    search_deplicatedモジュールのテストをするクラス
    '''

    def test_search_deplicated(self):
        '''
        関数のテストを行う
        '''

        list = ["アンパンマン" , "ばいきんまん" , "ジャムおじさん"]
        expect = [False , False , True]
        for idx , value in enumerate(list):
            result = search_deplicated.search_deplicated(value)
            self.assertEqual(result , expect[idx])

if __name__ == "__main__":
    unittest.main(verbosity=2)



