# Методы Юнит-тестирования

import unittest
import runner_and_tournament as rat

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)
        self.dist = 90


    # @classmethod
    # def tearDownClass(cls):
    #     # print(cls.all_results)

    def tearDown(self):
        print(self.all_results)


    def _test_tour(self, *participants):

        first = participants[1]
        last = participants[-1] # находим самого медленного бегуна и самого быстрого
        for i in participants:
            if i.speed > first.speed:
                first = i
            if i.speed < last.speed:
                last = i
        first, last = str(first), str(last)

        tour_obj = rat.Tournament(self.dist, *participants)
        all_results = tour_obj.start()
        all_results = {i: str(j) for i, j in all_results.items()}
        msg = f'Ошибка на дистанции {self.dist}: {first} должен быть первым, {last} - последним'

        return (f'{all_results}  (дистанция = {self.dist})',
                all_results[min(all_results.keys())] == first and all_results[max(all_results.keys())] == last,
                msg)


    def test_tour90_1(self):
        self.all_results, res, msg = self._test_tour(self.runner1, self.runner3)
        self.assertTrue(res, msg)

    def test_tour90_2(self):
        self.all_results, res, msg = self._test_tour(self.runner2, self.runner3)
        self.assertTrue(res, msg)

    def test_tour90_3(self):
        self.all_results, res, msg = self._test_tour(self.runner1, self.runner2, self.runner3)
        self.assertTrue(res, msg)

    def test_tour_6_3(self):
        # Если дистанция меньше, чем скорость последнего *2, то он "приходит вторым"
        self.dist = 6

        self.all_results, res, msg = self._test_tour(self.runner1, self.runner2, self.runner3)
        self.assertTrue(res, msg)






