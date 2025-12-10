from z3 import Optimize, Int, Sum, Product, And


def solve_machine(counters, buttons):
    optimize = Optimize()
    matrices = []
    for button in buttons:
        matrix = [0]*len(counters)
        for index in button:
            matrix[index] = 1
        matrices.append(matrix)
    coefficients = [Int(f"p{i}") for i in range(len(buttons))]
    equations = []
    for i in range(len(counters)):
        equations.append(Sum(*[Product(coefficient, matrices[j][i]) for j, coefficient in enumerate(coefficients)]) == counters[i])
    equations.extend([coefficient >= 0 for coefficient in coefficients])
    optimize.add(And(*equations))
    presses = Int("presses")
    optimize.add(presses == Sum(*coefficients))
    optimize.minimize(presses)
    optimize.check()
    return int(str(optimize.model().eval(presses)))
