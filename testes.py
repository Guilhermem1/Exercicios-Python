import unittest

from atividades import comer,dormir, eh_engracado

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando comida saudavel"""
        self.assertEqual(
            comer('quiado',True),  #a
            'Estou comendo quiado porque quero manter a forma'  #b
        )
    def teste_comer_gostosa(self):
        """Testando comida gostosa"""
        self.assertEqual(
            comer(comida='pizza',eh_saudavel=False),
            'Estou comendo pizza porque a gente se vive só uma vez'
        )

    def test_dormir_pouco(self):
        """Testando dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir 4 horas'
        )

    def test_dormir_muito(self):
        """Testando dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Dormi muito, estou atrasado'
        )

    def test_eh_engracado(self):
        self.assertEqual(eh_engracado('Sérgio Malandro'), False)
        #self.assertFalse(eh_engracado('Sérgio Malandro'))
        # Ao usar pass na funcao no modulo de atividades.py, ele retorna None, assim, para
        # self.assertFalse(eh_engracado('Sérgio Malandro')) é dado como OK porque None é dado como False ou true
        # logo, o correto seria fazer self.assertEqual((eh_engracado('Sérgio Malandro'),False)) pois desse modo
        # verifica se pessoa é de fato False e nao None
        self.assertTrue(eh_engracado('Jim carrey'),'Jim Carrey é muito engraçado')



if __name__ == '__main__':
    unittest.main()