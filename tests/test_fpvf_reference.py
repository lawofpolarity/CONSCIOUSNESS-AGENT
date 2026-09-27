import unittest
from src.fpvf_reference import *

class FPVFReferenceTests(unittest.TestCase):
    def test_fpvf_is_product(self):
        self.assertEqual(fpvf(2,lambda n:n+1,lambda n:2),6)

    def test_weighted_memory(self):
        self.assertEqual(weighted_memory([1,2,3],[2,3,4],2),20)

    def test_derivative_approximation(self):
        self.assertAlmostEqual(finite_difference(lambda x:x*x,2,1e-6),4,places=4)

    def test_trapezoid_constant(self):
        self.assertAlmostEqual(trapezoid_projection(3,lambda _:2,lambda _:4,20),24)

    def test_unified_is_declared_sum(self):
        self.assertEqual(unified(3,5),8)

    def test_invalid_inputs_fail(self):
        with self.assertRaises(ValueError):finite_difference(lambda x:x,0,0)
        with self.assertRaises(ValueError):weighted_memory([1],[1,2],0)

if __name__=="__main__":unittest.main()
