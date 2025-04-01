from dataclasses import dataclass

@dataclass
class Metodo:
    code: str
    type: str

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)