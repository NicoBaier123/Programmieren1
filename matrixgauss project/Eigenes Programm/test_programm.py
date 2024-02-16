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
    
    
    def test_linear_independent_matrix(self):
        A = np.matrix([
            [2, 1, 3],
            [1, 3, 2],
            [3, 2, 1]
        ])
        result = check_linear_dependency(A)
        expected_output = "Die Vektoren sind linear unabhängig."
        self.assertEqual(result, expected_output)

    def test_linear_dependent_matrix(self):
        A = np.matrix([
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ])
        result = check_linear_dependency(A)
        expected_output = "Die Vektoren sind linear abhängig. Die Lösungswerte für die Parameter sind:\n{}\n\nLösungsweg wurde in 'solution_steps.txt' gespeichert."
        self.assertEqual(result, expected_output)

    def test_underdetermined_matrix(self):
        A = np.matrix([
            [2, 0, 4],
            [0, 3, 5],
            [0, 0, 0]
        ])
        result = check_linear_dependency(A)
        expected_output = "Die Vektoren sind linear abhängig. Die Lösungswerte für die Parameter sind:\n{}\n\nLösungsweg wurde in 'solution_steps.txt' gespeichert."
        self.assertEqual(result, expected_output)

    def test_5x5_matrix(self):
        A = np.matrix([
            [1, 2, 3, 4, 5],
            [2, 7, 2, 0, -10],
            [3, 5, 8, 2, -32],
            [4, 3, 2, 1, 0],
            [5, 0, 9, 2, -2]
        ])
        result = check_linear_dependency(A)
        expected_output = "Die Vektoren sind linear unabhängig."
        self.assertEqual(result, expected_output)


    def test_variable_in_matrix(self):
        A = np.matrix([
            [1-a, 2, 3],
            [2, 4+b, 6],
            [3, 6, 9]
        ])
        result = check_linear_dependency(A)
        expected_output = "Die Vektoren sind linear abhängig, wenn die Variablen sind bestimmte Werte annehmen. Zum Beispiel: x3 = 0.5 * x2."
        self.assertEqual(result, expected_output)

    def test_unknownError(self):
        A = np.matrix([
            [2, 1, 4],
            [-1, 7, -5],
            [5, 0, 11]
        ])
        result = check_linear_dependency(A)
        expected_output = "Die Vektoren sind linear unabhängig."
        self.assertEqual(result, expected_output)

   
if __name__ == '__main__':
    unittest.main()
