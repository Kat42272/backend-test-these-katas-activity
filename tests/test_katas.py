import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        result = katas.add(10, 5)
        self.assertEqual(result, 15)
        # self.fail("TODO: Write add unit test")

    def test_multiply(self):
        result = katas.multiply(6, 5)
        self.assertEqual(result, 30)
        # self.fail("TODO: Write multiply unit test")

    def test_power(self):
        result = katas.power(2, 3)
        self.assertEqual(result, 8)
        # self.fail("TODO: Write power unit test")

    def test_factorial(self):
        result = katas.factorial(4)
        self.assertEqual(result, 24)
        # self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        result = katas.fibonacci(10)
        self.assertEqual(result, 55)
        # self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
