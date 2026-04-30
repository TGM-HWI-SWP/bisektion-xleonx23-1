import math
import matplotlib.pyplot as plt

class BaseSolver:
    def __init__(self, func_str: str) -> None:
        self.func_str = func_str
    def _evaluate(self, expression: str, x: float) -> float:
        return eval(expression, {"__builtins__": None}, {"x": x, "math": math})

class BisectionSolver(BaseSolver):
    def solve(self, a, b, tol=1e-7): # Minimalversion für Visualisierung
        pass

def visualize_bisection(func: str, a: float, b: float, iterations: int = 20):
    solver = BisectionSolver(func)
    x_vals, error_vals = [], []
    f = lambda x: solver._evaluate(func, x)
    for _ in range(iterations):
        c = (a + b) / 2
        x_vals.append(c)
        error_vals.append(abs(f(c)))
        if f(a) * f(c) < 0: b = c
        else: a = c
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(error_vals)
    plt.title("Fehler pro Iteration")
    plt.subplot(2, 1, 2)
    plt.plot(x_vals)
    plt.title("Annäherung an Lösung")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_bisection("x**2 - 25", 0, 50)