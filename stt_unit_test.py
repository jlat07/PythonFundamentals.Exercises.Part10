import unittest
import unittest.mock
from io import StringIO
import small_town_teller


class ListUtilsTest(unittest.TestCase):

    def test_add_Person(self):
        list_in = ['Bicycle', 'Scooter', 'Motorcycle', 'Car', 'Jet ski', 'RV', 'Motorboat']
        positions = [0, 1, 2, 3, -3, -2, -1]

        for item, position in zip(list_in, positions):
            with self.subTest(f"{item}, {position}"):
                self.assertEqual(item, list_utils.get_item_at_position(list_in, position))

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_list_items(self, mock_stdout):
        list_in = ['one', 'two', 'three', 'four']
        list_utils.print_list_items(list_in)
        self.assertEqual("\n".join(list_in) + "\n", mock_stdout.getvalue())

    def test_sort_by_commit_count(self):
        list_in = [
            ['joe', 15],
            ['alice', 30],
            ['jane', 28],
            ['bob', 42]
        ]
        expected_out = [
            ['joe', 15],
            ['jane', 28],
            ['alice', 30],
            ['bob', 42]
        ]
        self.assertEqual(expected_out, list_utils.sort_by_commit_count(list_in))

    def test_gen_list_of_nums(self):
        expected_out = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected_out, list_utils.gen_list_of_nums(10))

    def test_half_list(self):
        test_cases = [
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4], 1),  # first half even size list
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], 2),  # second half even size list
            ([0, 1, 2, 3, 4], [0, 1, 2], 1),  # first half odd size list
            ([0, 1, 2, 3, 4], [2, 3, 4], 2)  # second half odd size list
        ]
        for list_in, list_out, half_param in test_cases:
            with self.subTest(f"{list_in}, {half_param} -> {list_out}"):
                self.assertEqual(list_out, list_utils.half_list(list_in, half_param))

    def test_remove_account(self):
        list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_out = [0, 2, 4, 6, 8]
        stt_utils.remove_account(list_in)
        self.assertEqual(expected_out, list_in)

    def test_remove_evens(self):
        list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_out = [1, 3, 5, 7, 9]
        list_utils.remove_evens(list_in)
        self.assertEqual(expected_out, list_in)

    def test_concatenate_lists(self):
        test_cases = [
            ([1, 2], [1, 2], [1, 2, 1, 2]),
            ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
            (['A', 'B', 'C'], ['D', 'E', 'F'], ['A', 'B', 'C', 'D', 'E', 'F']),
            (['apples', 'bananas'], ['tomato', 'carrot'], ['apples', 'bananas', 'tomato', 'carrot'])

        ]
        for list_a, list_b, expected in test_cases:
            with self.subTest(f"{list_a}, {list_b} -> {expected}"):
                self.assertEqual(expected, list_utils.concatenate_lists(list_a, list_b))

    def test_multiply_list(self):
        test_cases = [
            ([1], 3, [1, 1, 1]),
            (['a'], 4, ['a', 'a', 'a', 'a'])
        ]
        for list_in, scalar, expected in test_cases:
            with self.subTest(f"{list_in}, {scalar} -> {expected}"):
                self.assertEqual(expected, list_utils.multiply_list(list_in, scalar))








    
    james = Person(01, 'James', 'Thompson')
    bob = Person(02, 'Bob', 'Smith')
    jane = Person(03, 'Jane', 'Johnson')
    
    james_savings = Account(1001, "SAVINGS_ACCOUNT", james)
    bob_checking = Account(1002, "CHECKING_ACCOUNT", bob)
    jane_investment = Account(1003, "INVESTMENT_ACCOUNT", jane)
    
    zc_bank = Bank()
    
    zc_bank.add_customer(james)
    zc_bank.add_customer(bob)
    zc_bank.add_customer(jane)
    
    zc_bank.add_account(james_savings)
    zc_bank.add_account(bob_checking)
    zc_bank.add_account(jane_investment)
    
    zc_bank.deposit(1003, 100)
    zc_bank.deposit(1002, 500)
    zc_bank.deposit(1001, 999999999)
    
    zc_bank.withdrawal(101, 1)
    zc_bank.withdrawal(102, 100)
    zc_bank.withdrawal(103, 50)
    
    
    
    
    