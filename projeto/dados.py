class Veiculo:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.motorista = None

class Motorista:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.veiculos = []