import math
from typing import Optional

def solver2():
    class BaseSolver:
        def __init__(self, func_str: str) -> None:
            self.func_str = func_str

        def _evaluate(self, expression: str, x: float) -> float:
            try:
                return eval(expression, {"__builtins__": None}, {"x": x, "math": math})
            except Exception as error:
                raise ValueError(f"Fehler im Ausdruck: {error}")

    class NewtonSolver(BaseSolver):
        def __init__(self, func_str: str, deriv_str: str) -> None:
            super().__init__(func_str)
            self.deriv_str = deriv_str

        def solve(self, x0: float, tol: float = 1e-7, max_iter: int = 100) -> Optional[float]:
            x = x0
            try:
                for _ in range(max_iter):
                    fx = self._evaluate(self.func_str, x)
                    dfx = self._evaluate(self.deriv_str, x)
                    if abs(dfx) < 1e-12:
                        raise ZeroDivisionError("Ableitung zu klein!")
                    x_new = x - fx / dfx
                    if abs(x_new - x) < tol:
                        return x_new
                    x = x_new
                raise RuntimeError("Max Iterationen erreicht")
            except Exception as error:
                print(f"Newton Fehler: {error}")
                return None

    test_values = [25, 81, 144]
    print("\n--- TEST NEWTON (Aufgabe 6) ---")
    for n in test_values:
        func, deriv, exact = f"x**2 - {n}", "2*x", math.sqrt(n)
        n_solver = NewtonSolver(func, deriv)
        n_result = n_solver.solve(n / 2)
        print(f"n={n:<3} | Ergebnis: {n_result:.6f} | Abweichung: {abs(n_result - exact):.2e}")

if __name__ == "__main__":
    solver2()