from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from source.utils import split_axiom


class Rule:

    def __init__(self, lhs, rhs):
        # Left hand side (input)
        self.lhs = lhs
        # Right hand side (output)
        self.rhs = rhs

    def __repr__(self):
        return 'Rule()'

    def __str__(self):
        return f'{self.lhs} -> {self.rhs}'


class L_system:

    def __init__(self, variables, constants, axiom, rules, N=8):
        # Alphabet
        self.variables = variables
        # Constants
        self.constants = constants
        # Axiom
        self.axiom = axiom
        # Production rules
        self.rules = rules
        # Store the number of thread
        self.N = N
        self.pool = ThreadPool(N)

    def next_generation(self):
        # Multiprocessing method
        results = self.pool.map(
            lambda axiom: self.compute_new_axiom(axiom),
            split_axiom(self.axiom, self.N)
            )
        # Reconstrust the axiom from the results
        self.axiom = ''
        for result in results:
            self.axiom += ''.join(result)

    def compute_new_axiom(self, axiom):
        new_axiom = ''
        for value in axiom:
            if value in self.constants:
                new_axiom += value
            else:
                for rule in self.rules:
                    if value == rule.lhs:
                        for new_value in rule.rhs:
                            new_axiom += new_value
                        break
        return new_axiom

