# Definindo a classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Dicionário para mapear o tipo de herói ao seu método de ataque
        ataques = {
            'mago': 'usou magia',
            'guerreiro': 'usou espada',
            'monge': 'usou artes marciais',
            'ninja': 'usou shuriken'
        }

        # Obtendo o ataque com base no tipo do herói
        ataque = ataques.get(self.tipo, 'não possui um ataque definido')

        # Exibindo a mensagem de ataque
        print(f"O {self.tipo} {self.nome} atacou usando {ataque}")

# Criando objetos heróis
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi2 = Heroi("Merlin", 45, "mago")
heroi3 = Heroi("Lee", 25, "monge")
heroi4 = Heroi("Hanzo", 35, "ninja")

# Heróis atacando
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
