import unittest
from robo import Robo

'''
class RoboTestes(unittest.TestCase):
    def test_carregar(self):
        megamen = Robo('Mega Men',bateria=50)
        megamen.carregar()
        self.assertEqual(megamen.bateria, 100)

    def test_dizer_nome(self):
        megamen = Robo('Mega Men',bateria=50)
        self.assertEqual(megamen.dizer_nome(),'BEEP BOOP EU SOU UM ROBO QUE SE CHAMA MEGA MEN')
        self.assertEqual(megamen.bateria, 49, 'A bateria deveria estar descarregando')
'''
# Utilizando o def setUp(self):
class RoboTestes(unittest.TestCase):
    def setUp(self):
        self.megamen = Robo('Mega Men',bateria=50)
        print('SetUp() sendo executado antes...')


    def test_carregar(self):
        self.megamen.carregar()
        self.assertEqual(self.megamen.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megamen.dizer_nome(),'BEEP BOOP EU SOU UM ROBO QUE SE CHAMA MEGA MEN')
        self.assertEqual(self.megamen.bateria, 49, 'A bateria deveria estar descarregando')

    def tearDown(self):
        print("tearDown() executado após a execucao...")


if __name__ == '__main__':
    unittest.main()

