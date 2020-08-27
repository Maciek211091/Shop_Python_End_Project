from Products_Class import T_Shirt
import unittest
import Custom_Exceptions


class Instance_Test(unittest.TestCase):


    def test_str(self):
        test_t_shirt = T_Shirt("Man", "XL", 5, "Blue")
        self.assertEqual(str(test_t_shirt), "Man T-Shirt, size XL, current stock 5")

    def test_instance(self):
        test_t_shirt = T_Shirt("Man", "XL", 5, "Blue")
        return self.assertEqual(isinstance(test_t_shirt, T_Shirt), True)

    def test_add_stock(self):
        test_t_shirt = T_Shirt("Man", "XL", 5, "Blue")
        test_t_shirt.add_stock(5)
        value_to_check = test_t_shirt.get_num_of_el()
        self.assertEqual(value_to_check, 10)

    def test_reduce1(self):
        test_t_shirt = T_Shirt("Man", "XL", 5, "Blue")
        test_t_shirt.reduce_stock(2)
        value_to_check = test_t_shirt.get_num_of_el()
        self.assertEqual(value_to_check, 3)

    def test_reduce2(self):
        with self.assertRaises(Exception) as context:
            test_t_shirt = T_Shirt("Man", "XL", 5, "Blue")
            test_t_shirt.reduce_stock(7)
            self.assertTrue(Custom_Exceptions.Less_Than_Zero_Exception, context.exception)
