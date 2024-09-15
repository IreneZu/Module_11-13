#  Систематизация и пропуск тестов
#  Задача "Заморозка кейсов":

import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_obj = Runner('Mike')
        [run_obj.walk() for _ in range(10)]
        self.assertEqual(run_obj.distance, 50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_obj = Runner('Mike')
        [run_obj.run() for _ in range(10)]
        self.assertEqual(run_obj.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_obj1 = Runner('Mike')
        run_obj2 = Runner('Nike')

        [(run_obj1.walk(), run_obj2.run()) for _ in range(10)]

        self.assertNotEqual(run_obj1.distance, run_obj2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)
        self.dist = 90


    # @classmethod
    # def tearDownClass(cls):
    #     # print(cls.all_results)

    # def tearDown(self):
    #     print(self.all_results)


    def _test_tour(self, *participants):

        first = participants[1]
        last = participants[-1] # находим самого медленного бегуна и самого быстрого
        for i in participants:
            if i.speed > first.speed:
                first = i
            if i.speed < last.speed:
                last = i
        first, last = str(first), str(last)

        tour_obj = Tournament(self.dist, *participants)
        all_results = tour_obj.start()
        all_results = {i: str(j) for i, j in all_results.items()}
        msg = f'Ошибка на дистанции {self.dist}: {first} должен быть первым, {last} - последним'

        return (f'{all_results}  (дистанция = {self.dist})',
                all_results[min(all_results.keys())] == first and all_results[max(all_results.keys())] == last,
                msg)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tour90_1(self):
        self.all_results, res, msg = self._test_tour(self.runner1, self.runner3)
        self.assertTrue(res, msg)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tour90_2(self):
        self.all_results, res, msg = self._test_tour(self.runner2, self.runner3)
        self.assertTrue(res, msg)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tour90_3(self):
        self.all_results, res, msg = self._test_tour(self.runner1, self.runner2, self.runner3)
        self.assertTrue(res, msg)

    @unittest.skip('Тест с ошибкой на малой дистанции пропускаем')
    def test_tour_6_3(self):
        # Если дистанция меньше, чем скорость последнего *2, то он "приходит вторым"
        self.dist = 6

        self.all_results, res, msg = self._test_tour(self.runner1, self.runner2, self.runner3)
        self.assertTrue(res, msg)

if __name__ == '__main__':
    unittest.main()

#  Вопрос преподавателю к вебинару: зачем нужны 2 последние строчки (как в лекции), вроде и без них выполняется


