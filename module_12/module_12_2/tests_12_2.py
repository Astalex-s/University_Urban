import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner("Усэйн", 10)
        self.runner2 = rat.Runner("Андрей", 9)
        self.runner3 = rat.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(f'{i}:')
            print({k: str(v) for k, v in cls.all_results[i].items()})

    def test1(self):
        tournament1 = rat.Tournament(90, self.runner1, self.runner3)
        result = tournament1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Первый раунд'] = result

    def test2(self):
        tournament2 = rat.Tournament(90, self.runner2, self.runner3)
        result = tournament2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Второй раунд'] = result

    def test3(self):
        tournament3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Третий раунд'] = result


if __name__ == '__main__':
    unittest.main()
