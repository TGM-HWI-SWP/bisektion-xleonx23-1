from Aufgabe5 import solver
from Aufgabe6 import solver2
from Aufgabe7 import plotter
import math

def aufgabe_9():
    class BisectionSolver:
        def __init__(self, func_str: str):
            self.func_str = func_str

        def _evaluate(self, expression: str, x: float) -> float:
            return eval(expression, {"__builtins__": None}, {"x": x, "math": math})

        def solve(self, a: float, b: float, tol: float = 1e-7):
            f = lambda x: self._evaluate(self.func_str, x)
            f_a = f(a)
            f_b = f(b)
            
            if f_a * f_b >= 0:
                return None

            for _ in range(1000):
                c = (a + b) / 2
                f_c = f(c)
                
                if abs(f_c) < tol or (b - a) / 2 < tol:
                    return c
                
                if f_a * f_c < 0:
                    b = c
                else:
                    a = c
                    f_a = f_c
            return (a + b) / 2

    w = 100
    func = "x * math.cosh(50/x) - x - 10"
    
    solver_obj = BisectionSolver(func)
    a_res = solver_obj.solve(1, 1000)

    if a_res is not None:
        length = 2 * a_res * math.sinh(50 / a_res)
        print("\n--- SEILPROBLEM (Aufgabe 9) ---")
        print(f"Parameter a ≈ {a_res}")
        print(f"Gesamtlänge L ≈ {length} m")

if __name__ == "__main__":
    solver()
    solver2()
    plotter()
    aufgabe_9()