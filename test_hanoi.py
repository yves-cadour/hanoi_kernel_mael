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
        
    def testHanoi_statut0(self):
        status, move=self.hanoi.move(1,3)
        self.assertEqual(status, 0, f"le statut est à 0 il est a {status}")
        self.assertEqual(move, (1,3), f"le déplacement est à 1, 3 il est a {move}")
        
    def testHanoi_statut1(self):
        hanoi=Hanoi(2)
        hanoi.move(1,2)
        hanoi.move(1,3)
#         import pdb; pdb.set_trace()
        status, move=hanoi.move(2,3)
        self.assertEqual(status, 1, f"le statut est à 1 il est a {status}")
        self.assertEqual(move, (2,3), f"le déplacement est à 2, 3 il est a {move}")
        
    def testHanoi_statut1(self):
            hanoi=Hanoi(2)
            hanoi.move(1,2)
            hanoi.move(1,3)
    #         import pdb; pdb.set_trace()
            status, move=hanoi.move(2,3)
            self.assertEqual(status, 1, f"le statut est à 1 il est a {status}")
            self.assertEqual(move, (2,3), f"le déplacement est à 2, 3 il est a {move}")
        
    def testHanoi_statut2(self):
        self.hanoi.move(1,3)
        status, move=self.hanoi.move(1,3)
        self.assertEqual(status, 2, f"le statut est à 2 il est a {status}")
        self.assertEqual(move, (1,1), f"le move est à 1,1 il est a {move}")
        
    def testHanoi_statut3(self):
        status, move=self.hanoi.move(1,1)
        self.assertEqual(status, 3, f"le statut est à 3 il est a {status}")
        self.assertEqual(move, (1,1), f"le déplacement est à 1, 1 il est a {move}")
        

    def testHanoi_statut4(self):
        status, move=self.hanoi.move(2,3)
        self.assertEqual(status, 4, f"le statut est à 4 il est a {status}")
        self.assertEqual(move, (), f"le déplacement est un tuple vide il est a {move}")
        
        
    def testHanoi_statut5(self):
        status, move =self.hanoi.move(1,4)
        self.assertEqual(status, 5, f"le statut est à 5 il est a {status}")
        status, move =self.hanoi.move(5,3)
        self.assertEqual(status, 5, f"le statut est à 5 il est a {status}")
        
    def testHistory(self):
        self.hanoi.move(1,3)
        self.hanoi.move(1,3)
        self.hanoi.move(1,2)
        self.hanoi.move(3,2)
        self.hanoi.move(1,3)
        self.hanoi.move(1,2)
        self.hanoi.move(2,1)
        self.hanoi.move(2,3)
        self.hanoi.move(1,3)
        result=self.hanoi.get_history()
        self.assertEqual(result, [(1,3),(1,2),(3,2),(1,3),(2,1),(2,3),(1,3)], f"l'historique n'est pas correct il est égal à {result} alors qu'il devrait être égal à [(1,3), (1,2),(3,2),(1,3),(2,1),(2,3),(1,3)]")
        

        
if __name__ == '__main__':
    unittest.main()  