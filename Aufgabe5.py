import math
from typing import Optional

def solver():


    class BaseSolver:
        """
        Basisklasse für Solver.
        Stellt dynamische Funktionsauswertung bereit.
        """

        def __init__(self, func_str: str) -> None:
            self.func_str = func_str

        def _evaluate(self, expression: str, x: float) -> float:
            """
            Wertet mathematischen Ausdruck aus.
            """
            try:
                return eval(expression, {"__builtins__": None}, {"x": x, "math": math})
            except Exception as error:
                raise ValueError(f"Fehler im Ausdruck: {error}")


    class BisectionSolver(BaseSolver):
        """
        Bisektionsverfahren zur Nullstellensuche.
        """

        def solve(self, a: float, b: float, tol: float = 1e-7,
                max_iter: int = 1000) -> Optional[float]:

            try:
                f_a = self._evaluate(self.func_str, a)
                f_b = self._evaluate(self.func_str, b)

                if f_a * f_b >= 0:
                    raise ValueError("Kein Vorzeichenwechsel!")

                for _ in range(max_iter):
                    c = (a + b) / 2
                    f_c = self._evaluate(self.func_str, c)

                    if abs(f_c) < tol:
                        return c

                    if f_a * f_c < 0:
                        b = c
                    else:
                        a = c
                        f_a = f_c

                    if (b - a) / 2 < tol:
                        return (a + b) / 2

                raise RuntimeError("Max Iterationen erreicht")

            except Exception as error:
                print(f"Bisektion Fehler: {error}")
                return None


    # -----------------------------------------
    # TEST (Aufgabe 5)
    # -----------------------------------------

    def run_software_test_bisection() -> None:
        test_values = [25, 81, 144]

        print("\n--- SOFTWARETEST BISEKTION ---")
        print(f"{'n':<5} | {'Methode':<10} | {'Ergebnis':<12} | {'Abweichung'}")
        print("-" * 50)

        for n in test_values:
            func = f"x**2 - {n}"
            exact = math.sqrt(n)

            b_solver = BisectionSolver(func)
            b_result = b_solver.solve(0, n)

            if b_result is not None:
                print(f"{n:<5} | Bisektion | {b_result:.6f} | {abs(b_result - exact):.2e}")

    if __name__ == "__main__":
        run_software_test_bisection()


if __name__ == "__main__":
    
    solver()