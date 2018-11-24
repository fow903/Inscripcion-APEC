from django.test import TestCase


class TestStringMethods(TestCase):

    def test_aula_len(self,aula):
        self.assertEqual(len(aula), 5)

    def test_modulo_no_negativo(self,modulo):
        assert (modulo >= 0),"Modulo no puede ser negativo"

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
