class Person: 
    def __init__(self, nome, vida, ataque, defesa, regen):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.regen = regen

    def __str__(self):
        return f"{self.nome} [HP:{self.vida} ATK:{self.ataque} DEF:{self.defesa} REG:{self.regen}]"

    def __repr__(self):
        return f"Person({self.nome!r}, {self.vida}, {self.ataque}, {self.defesa}, {self.regen})"

Frankly = Person("Frankly Andrew", 200, 10, 10, 2)