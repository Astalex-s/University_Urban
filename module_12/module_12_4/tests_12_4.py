import unittest
import rt_with_exceptions
import logging

logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                        format='%(asctime)s, %(levelname)s, %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test1 = rt_with_exceptions.Runner('Alex', -10)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                test1.walk()
            self.assertEqual(test1.distance, 50)
        except Exception as e:
            logging.warning('Неверная скорость для Runner.', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test2 = rt_with_exceptions.Runner(11111)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                test2.run()
            self.assertEqual(test2.distance, 100)
        except Exception as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test1 = rt_with_exceptions.Runner(name='Alex')
        test2 = rt_with_exceptions.Runner(name='Max')
        for _ in range(10):
            test1.walk()
            test2.run()
        self.assertNotEqual(test1.distance, test2.distance)


if __name__ == '__main__':
    unittest.main()


