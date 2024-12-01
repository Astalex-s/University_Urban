import unittest
import tests_12_3


rat_TS = unittest.TestSuite()
rat_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
rat_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(rat_TS)
