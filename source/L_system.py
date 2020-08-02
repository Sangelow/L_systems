from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from source.utils import split_axiom


class L_system:

    def __init__(self, variables, constants, axiom, rules, N=cpu_count()):
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
                new_axiom += self.rules[value]
        return new_axiom

