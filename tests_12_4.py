import unittest
import logging
from rt_with_exceptions import Runner

# print(__name__)
# if __name__ == '__main__':
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8'
                    , format='\n%(asctime)s |  %(levelname)s --- %(message)s')
print('См. лог файл "runner_tests.log" !')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            run_obj = Runner('Mike', -10)
            [run_obj.walk() for _ in range(10)]
            self.assertEqual(run_obj.distance, 50)

            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            run_obj = Runner(True, 20)
            [run_obj.run() for _ in range(10)]
            self.assertEqual(run_obj.distance, 100)

            logging.info(f'"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        run_obj1 = Runner('Mike')
        run_obj2 = Runner('Nike')

        [(run_obj1.walk(), run_obj2.run()) for _ in range(10)]

        self.assertNotEqual(run_obj1.distance, run_obj2.distance)



# if __name__ == '__main__':
#     unittest.main()


