import unittest
import numpy as np
from MatrixCalc import check_linear_dependency
#linear abhängig - unendlich lösung - lösung in abhängigkeit von x1
#lösbar - konkrete Lösungsmenge ausgeben
#Nullkombinationen (z.B. in der ersten Zeile)
#konstanten mit drin -für welche Werte der Konstanten lösbar/linear abhängig (unter welchen Umständen)
class check_dependency(unittest.TestCase):
    
    def test_funktion_zum_testen_positive(self):
        A = np.matrix([ [1, 2], 
                        [2, 4]])
        result = check_linear_dependency(A)
        expected_output ="Die Vektoren sind linear abhängig. Die Lösungswerte für die Parameter sind:\n{}\n\nLösungsweg wurde in 'solution_steps.txt' gespeichert."
        self.assertEqual(result, expected_output)
    
    def test_underdetermined_matrix(self):
        A = np.matrix([
            [2, 0, 4],
            [0, 3, 5],
            [0, 0, 0]
        ])
        result = check_linear_dependency(A)
        expected_output = "Das Gleichungssystem ist unterbestimmt."
        self.assertEqual(result, expected_output)

   
    def test_variable_in_matrix(self):
        A = np.matrix([
            [1-a, 2, 3],
            [2, 4+b, 6],
            [3, 6, 9]
        ])
        result = check_linear_dependency(A)
        expected_output = "Das Gleichungssystem ist linear abhängig. Die Variablen sind linear abhängig, zum Beispiel: x3 = 0.5 * x2."
        self.assertEqual(result, expected_output)

    def test_regular_matrix(self):
        A = np.matrix([
            [2, 1, 3],
            [1, 3, 2],
            [3, 2, 1]
        ])
        result = check_linear_dependency(A)
        expected_output = "Das Gleichungssystem hat eine eindeutige Lösung. Die Matrix ist linear unabhängig."
        self.assertEqual(result, expected_output)

    def test_linear_dependent_matrix(self):
        A = np.matrix([
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ])
        result = check_linear_dependency(A)
        expected_output = "Das Gleichungssystem ist linear abhängig. Die Matrix hat Zeilen, die linear abhängig sind."
        self.assertEqual(result, expected_output)

    # Füge hier weitere Testmethoden hinzu

if __name__ == '__main__':
    unittest.main()
