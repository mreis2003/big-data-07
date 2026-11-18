total_despesas = 0.0
quantidade_despesas = 0

continuar = "s"

while continuar.lower() != "n":
    valor = float(input("Digite o valor da despesa: R$ "))

    if valor > 0:
        total_despesas += valor
        quantidade_despesas += 1
    else:
        print("Informe um valor válido!")

    continuar = input("Deseja registrar outra despesa? (S/N): ")

# Exibição do resultado final
print("\n===== RESUMO DAS DESPESAS =====")
print(f"Quantidade de despesas registradas: {quantidade_despesas}")
print(f"Valor total das despesas: R$ {total_despesas:.2f}")