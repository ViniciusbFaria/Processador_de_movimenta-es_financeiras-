import csv
from copy import deepcopy

saldos = {}
inconsistencias = []
total_C = 0.0
total_D = 0.0
quantidade = 0
duplicados = []
registros_vistos = set()
fechamento_diario = {}
rollbacks = []

with open("data/relatorio.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")

    cabecalho = next(arquivo_csv)

    for linha in arquivo_csv:
        data = linha[0]
        conta = linha[1]
        tipo = linha[2]
        valor = float(linha[3])
        descricao = linha[4]

        registro = (data, conta, tipo, valor, descricao)

        if registro in registros_vistos:
            duplicados.append(registro)
            continue
        registros_vistos.add(registro)

        if conta not in saldos:
            saldos[conta] = 0.0

        if tipo == "C":
            saldos[conta] += valor
            total_C += valor

        elif tipo == "D":

            if saldos[conta] - valor < 0:
                rollbacks.append((conta, data, descricao))
                continue
            saldos[conta] -= valor
            total_D += valor

        quantidade += 1

        if saldos[conta] < 0:
            inconsistencias.append((conta, data, descricao))

        if data not in fechamento_diario:
            fechamento_diario[data] = deepcopy(saldos)
        else:
            fechamento_diario[data][conta] = saldos[conta]

print("saldo final por conta:")
for conta in sorted(saldos):
    print(f"{conta}: {saldos[conta]:.2f}")

print("\nResumo das movimentaçoes:")
print(f"Total de créditos: {total_C:.2f}")
print(f"Total de débitos: {total_D:.2f}")
print(f"Quantidade de lançamentos: {quantidade}")

print("\nFechamento diario:")
for data in sorted(fechamento_diario):
    print(f"\nData: {data}")
    for conta, saldo in fechamento_diario[data].items():
        print(f"  {conta}: {saldo:.2f}")

print("\nInconsistencias:")
if inconsistencias:
    for erro in inconsistencias:
        print(erro)
else:
    print("Nenhuma inconsistência encontrada.")

print("\nLançamentos duplicados:")
if duplicados:
    for dup in duplicados:
        print(dup)
else:
    print("Nenhum lançamento duplicado encontrado.")

print("\nRollbacks lógicos:")
if rollbacks:
    for rb in rollbacks:
        print(rb)
else:
    print("Nenhum rollback realizado.")
