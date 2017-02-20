from sys import argv
from modules.series import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import integrate, oo, limit
from sympy.abc import x
import math


def main():
    n = int(argv[1])
    terms = np.zeros(n, Decimal)
    sums = np.zeros(n, Decimal)

    padding = len(argv[1])
    # calculate n terms
    for i in range(0, n):
        index = i + 1
        terms[i] = (nth_term(index))

    sums[0] = nth_term(1)
    for i in range(1, n):
        # calculate n partial sums
        sums[i] = sums[i - 1] + terms[i]
        print("%s | %s" % (str(i + 1).rjust(padding), sums[i]))
    print()

    # check d'Alambert ratio
    x0 = math.inf
    ratio_limit = limit((x + 7) ** (-1/3) / ((x + 6) ** (-1/3)), x, x0)

    convergence = "divergent"
    if ratio_limit < 1:
        convergence = "convergent"
    elif ratio_limit == 1:
        convergence = "can't state"

    print("d'Alembert ratio: %s | %s" % (convergence, terms[n - 1] / terms[n - 2]))

    # check Cauchy ratio
    I = integrate((x + 6) ** (-1 / 3), x, (x, 1, oo))
    is_convergent = I != math.inf and I != -math.inf
    print("Cauchy ratio: %s" % ("convergent" if is_convergent else "divergent"))

    # partial sums plot
    plt.plot(range(1, n + 1), sums)
    plt.title("Partial sum of series")
    plt.ylabel("\u03A3\u1D62")
    plt.xlabel("n")
    plt.show()

    # terms plot
    plt.plot(range(1, n+1), terms)
    plt.title("Series terms")
    plt.ylabel("n\u1D62")
    plt.xlabel("i")
    plt.show()

if __name__ == "__main__":
    main()