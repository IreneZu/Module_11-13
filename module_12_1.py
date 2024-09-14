import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run_obj = Runner('Mike')
        [run_obj.walk() for _ in range(10)]
        self.assertEqual(run_obj.distance, 50)

    def test_run(self):
        run_obj = Runner('Mike')
        [run_obj.run() for _ in range(10)]
        self.assertEqual(run_obj.distance, 100)

    def test_challenge(self):
        run_obj1 = Runner('Mike')
        run_obj2 = Runner('Nike')

        [(run_obj1.walk(), run_obj2.run()) for _ in range(10)]

        self.assertNotEqual(run_obj1.distance, run_obj2.distance)

