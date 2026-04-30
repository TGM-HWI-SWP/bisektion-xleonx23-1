import math

def aufgabe_8():
    class BisectionSolver:
        def __init__(self, func_str: str):
            self.func_str = func_str

        def _evaluate(self, expression: str, x: float) -> float:
            return eval(expression, {"__builtins__": None}, {"x": x, "math": math})

        def solve(self, a: float, b: float, tol: float):
            f = lambda x: self._evaluate(self.func_str, x)
            iterations = 0
            
            while (b - a) / 2 > tol:
                c = (a + b) / 2
                if f(a) * f(c) < 0:
                    b = c
                else:
                    a = c
                iterations += 1
            
            return (a + b) / 2, iterations

    func = "2*x + x**2 + 3*x**3 - x**4"
    solver = BisectionSolver(func)

    res_1, iter_1 = solver.solve(3, 4, 1e-2)
    res_2, iter_2 = solver.solve(3, 4, 1e-8)

    print("\n--- GENAUIGKEIT (Aufgabe 8) ---")
    print(f"Nullstelle (3, 4) ≈ {res_1}")
    print(f"Iterationen für ε=1e-2: {iter_1}")
    print(f"Iterationen für ε=1e-8: {iter_2}")

if __name__ == "__main__":
    aufgabe_8()