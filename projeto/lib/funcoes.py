# funcoes.py
from dados import Veiculo, Motorista

# Dicionários para armazenar veículos e motoristas
veiculos = {}
motoristas = {}

def cadastrar_veiculo(placa, modelo, ano):
    if placa not in veiculos:
        veiculos[placa] = Veiculo(placa, modelo, ano)
        return True
    return False

def consultar_veiculo(placa):
    return veiculos.get(placa)

def atualizar_veiculo(placa, modelo=None, ano=None):
    veiculo = consultar_veiculo(placa)
    if veiculo:
        if modelo:
            veiculo.modelo = modelo
        if ano:
            veiculo.ano = ano
        return True
    return False

def apagar_veiculo(placa):
    if placa in veiculos:
        del veiculos[placa]
        return True
    return False

def trocar_veiculo_motorista(placa, nome_motorista):
    veiculo = consultar_veiculo(placa)
    if veiculo:
        motorista = motoristas.get(nome_motorista)
        if motorista:
            veiculo.motorista = motorista
            motorista.veiculos.append(veiculo)
            return True
    return False

def cadastrar_motorista(nome, idade):
    if nome not in motoristas:
        motoristas[nome] = Motorista(nome, idade)
        return True
    return False

def consultar_motorista(nome):
    return motoristas.get(nome)

def atualizar_motorista(nome, idade):
    motorista = consultar_motorista(nome)
    if motorista:
        motorista.idade = idade
        return True
    return False

def apagar_motorista(nome):
    if nome in motoristas:
        del motoristas[nome]
        return True
    return False

def veiculos_do_motorista(nome_motorista):
    motorista = consultar_motorista(nome_motorista)
    if motorista:
        return motorista.veiculos
    return []

def listar_todos_veiculos():
    return list(veiculos.values())

def listar_motoristas():
    return list(motoristas.values())