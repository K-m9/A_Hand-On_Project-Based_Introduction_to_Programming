# -*- coding:utf-8 -*-
# author:Karen time:2020/8/5

import unittest
import city_functions


class test_city_country(unittest.TestCase):
    '''test test_cities.py, only for the function with return value.
    (without return value: https://blog.csdn.net/python012/article/details/79903641)
    '''

    def test_city_country(self):
        city_country = city_functions.city_functions('guangzhou', 'china',500000)
        self.assertEqual(city_country, 'Guangzhou, China - population 500000')

unittest.main()
