import unittest
import numpy as np
from MatrixCalc import gauss_elimination
#linear abhängig - unendlich lösung - lösung in abhängigkeit von x1
#lösbar - konkrete Lösungsmenge ausgeben
#Nullkombinationen (z.B. in der ersten Zeile)
#konstanten mit drin -für welche Werte der Konstanten lösbar/linear abhängig (unter welchen Umständen)
class check_linear_dependency(unittest.TestCase):
    
    def test_funktion_zum_testen_positive(self):
        A = np.matrix([ [1, 2], 
                        [2, 4]])
        result = gauss_elimination(A)
        expected_output = f"Die Gleichungen sind unterbestimmt. Die Lösungs Menge ist L ={np.array("x_1=-2*x_2",  "x_2=x_2")} "
        self.assertEqual(result, expected_output)


    # Füge hier weitere Testmethoden hinzu

if __name__ == '__main__':
    unittest.main()
