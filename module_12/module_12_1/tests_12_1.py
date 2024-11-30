import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test1 = runner.Runner(name='Alex')
        for _ in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    def test_run(self):
        test2 = runner.Runner(name='Max')
        for _ in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    def test_challenge(self):
        test1 = runner.Runner(name='Alex')
        test2 = runner.Runner(name='Max')
        for _ in range(10):
            test1.walk()
            test2.run()
        self.assertNotEqual(test1.distance, test2.distance)


if __name__ == '__main__':
    unittest.main()
