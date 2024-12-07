import unittest
from print_queue import find_sum_of_middle_nums
from print_queue import arrange_order_rules_per_key
from print_queue import find_right_ordered_updates
from print_queue import order_page_correctly
from print_queue import is_page_in_right_order
from print_queue import find_corrected_pages

class PrintQueueTestCase(unittest.TestCase):
    def test_is_page_in_right_order(self):
        ordering_rules = {'47': {'13', '53', '61', '29'}, '97': {'75', '13', '53', '29', '61', '47'}, '75': {'13', '53', '29', '61', '47'}, '13': set(), '61': {'13', '53', '29'}, '29': {'13'}, '53': {'13', '29'}}

        result = is_page_in_right_order(ordering_rules, ['75','97','47','61','53'])
        expected =False
        self.assertEqual(result, expected)
    def test_find_right_ordered_updates(self):

        update_pages = [['75','47', '61', '53', '29'],
                 ['97','61','53','29','13'],
                 ['75','29','13'],
                 ['75','97','47','61','53'],
                 ['61','13','29'],
                 ['97','13','75','29','47']]
        ordering_rules = {'47': {'13', '53', '61', '29'}, '97': {'75', '13', '53', '29', '61', '47'}, '75': {'13', '53', '29', '61', '47'}, '13': set(), '61': {'13', '53', '29'}, '29': {'13'}, '53': {'13', '29'}}
       
        result = find_right_ordered_updates(ordering_rules, update_pages)
        expected = [['75', '47', '61', '53', '29'], ['97', '61', '53', '29', '13'], ['75', '29', '13']], [['75','97','47','61','53'],['61','13','29'],['97','13','75','29','47']]
        self.assertEqual(result, expected)
    def test_order_page(self):
        ordering_rules = {'47': {'13', '53', '61', '29'}, '97': {'75', '13', '53', '29', '61', '47'}, '75': {'13', '53', '29', '61', '47'}, '13': set(), '61': {'13', '53', '29'}, '29': {'13'}, '53': {'13', '29'}}
        result = order_page_correctly(ordering_rules, ['75','97','47','61','53'])
        expected = ['97','75','47','61','53']
        self.assertEqual(result, expected)

    def test_order_page_2(self):
        ordering_rules = {'47': {'13', '53', '61', '29'}, '97': {'75', '13', '53', '29', '61', '47'}, '75': {'13', '53', '29', '61', '47'}, '13': set(), '61': {'13', '53', '29'}, '29': {'13'}, '53': {'13', '29'}}
        result = order_page_correctly(ordering_rules, ['61','13','29'])
        expected =  ['61','29','13']
        self.assertEqual(result, expected)

    def test_order_page_3(self):
        ordering_rules = {'47': {'13', '53', '61', '29'}, '97': {'75', '13', '53', '29', '61', '47'}, '75': {'13', '53', '29', '61', '47'}, '13': set(), '61': {'13', '53', '29'}, '29': {'13'}, '53': {'13', '29'}}
        result = order_page_correctly(ordering_rules,['97','13','75','29','47'])
        expected =  ['97', '75', '47', '29', '13']
        self.assertEqual(result, expected)

    # def test_find_corrected_pages(self):
    #     ordering_rules = {'47': {'13', '53', '61', '29'}, '97': {'75', '13', '53', '29', '61', '47'}, '75': {'13', '53', '29', '61', '47'}, '13': set(), '61': {'13', '53', '29'}, '29': {'13'}, '53': {'13', '29'}}
    #     result = find_corrected_pages(ordering_rules,  [['75','97','47','61','53'],['61','13','29'],['97','13','75','29','47']])
    #     expected = [['97','75','47','61','53'], ['61','29','13'], ['97', '75', '47', '29', '13']]
    #     self.assertEqual(result, expected)

    def test_sum_of_mid_number(self):
        ordered_pages = [['75', '47', '61', '53', '29'], ['97', '61', '53', '29', '13'], ['75', '29', '13']]
        result = find_sum_of_middle_nums(ordered_pages)
        expecpted = 143
        self.assertEqual(result, expecpted)
    
    def test_arrange_order_rules_per_key(self):
        ordering_rules = [('47','53'), ('97','13'), ('97','61'), ('97','47'), ('75','29'),('61','13'),('75','53'),('29','13'),('97','29'),
                          ('53','29'),('61','53'),('97','53'),('61','29'),('47','13'),('75','47'),('97','75'),('47','61'),('75','61'),('47','29'),('75','13'),('53','13')]
        result = arrange_order_rules_per_key(ordering_rules)
        expected = {'47': {'13', '53', '61', '29'}, '97': {'75', '13', '53', '29', '61', '47'}, '75': {'13', '53', '29', '61', '47'}, '13': set(), '61': {'13', '53', '29'}, '29': {'13'}, '53': {'13', '29'}}
        self.assertEqual(result, expected)