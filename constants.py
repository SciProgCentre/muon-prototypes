ELECTRON_MASS = 9.10938356E-31  # GeV/c^2
AVOGADRO_NUMBER = 6.02214076E+23
MUON_MASS = 0.1056583745  # GeV/c^2


class AtomicElement:
    def __init__(self, A, I, Z):
        self.A = A  # Atomic mass
        self.I = I  # Mean Excitation
        self.Z = Z  # Atomic Number


STANDARD_ROCK = AtomicElement(22.0, 0.1364E-6, 11)
