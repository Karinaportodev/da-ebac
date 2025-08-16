
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina = pd.DataFrame({
    'dia': list(range(1, 11)),
    'venda': [4.96, 4.97, 4.97, 4.98, 4.99, 5.00, 5.00, 5.01, 5.02, 5.07]
})

gasolina.to_csv('gasolina.csv', index=False)

plt.figure(figsize=(8,5))
sns.lineplot(x='dia', y='venda', data=gasolina, marker='o')
plt.title('Preço médio da gasolina em São Paulo - Julho/2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.savefig('gasolina.png')
plt.show()
    