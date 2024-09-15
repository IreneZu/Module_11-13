#  Систематизация и пропуск тестов
#  Задача "Заморозка кейсов":

import unittest
import tests_12_3

ratTS = unittest.TestSuite()
ratTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ratTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test_run = unittest.TextTestRunner(verbosity=2)
test_run.run(ratTS)




