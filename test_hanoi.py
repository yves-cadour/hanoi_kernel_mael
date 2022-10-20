#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from hanoi_kernel import Hanoi

class StackTests(unittest.TestCase):
    """
    A class to test the Stack module
    """
    def setUp(self):
        """
        create an empty Stack for all tests
        """
        self.hanoi=Hanoi(3)
        
    def testHanoi