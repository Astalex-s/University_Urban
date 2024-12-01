import unittest
from module_12.module_12_2.runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test1 = Runner(name='Alex')
        for _ in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test2 = Runner(name='Max')
        for _ in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test1 = Runner(name='Alex')
        test2 = Runner(name='Max')
        for _ in range(10):
            test1.walk()
            test2.run()
        self.assertNotEqual(test1.distance, test2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(f'{i}:')
            print({k: str(v) for k, v in cls.all_results[i].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        result = tournament1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Первый раунд'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        result = tournament2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Второй раунд'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Третий раунд'] = result


if __name__ == '__main__':
    unittest.main()
