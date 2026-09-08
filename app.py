#Calculadora de Consumo Elétrico

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em Watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

consumo_mensal = (potencia * horas_dia *30) / 1000
custo_estimado = consumo_mensal * 0.75

print()
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.0f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")