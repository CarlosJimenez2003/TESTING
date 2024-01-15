from codi import funcio1

import unittest

class  test_Funcio1(unittest.TestCase): 
    def test_Funcio1_positiu(self):          #test_funcio1_positiu es el nom del test que anem a fer
        resultat = funcio1(1)                #El "resultat" de la funcio1 li enviem el parametre (1) per fer el test
        self.assertEqual(resultat, 1)        #(self).assertEqual --> auto test de que es igual el parametre de sortida que el de entrada
    
    def test_Funcio1_zero(self): 
        resultat = funcio1(0)
        self.assertEqual(resultat, 0)        #Al enviar el 0 la funcio "funcio1" retorna 0 i el assertEqual comprova que el valor retornat sige igual que el que hem introduit nosaltres
    
    def test_Funcio1_negatiu(self):
        resultat = funcio1(-3)
        self.assertEqual(resultat, -1)

if __name__=='__main__':
   unittest.main()