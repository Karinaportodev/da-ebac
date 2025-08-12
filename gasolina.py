import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler dados
df = pd.read_csv("gasolina.csv")

# Criar gráfico
plt.figure(figsize=(8,5))
sns.lineplot(x="dia", y="valor", data=df, marker="o")
plt.title("Preço médio da gasolina em São Paulo (Julho 2021)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)

# Salvar imagem
plt.savefig("gasolina.png")
plt.show()
