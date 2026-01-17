from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Dados do problema
# 1 = Falha (Positivo), 0 = Sucesso (Negativo)
y_true = [1] * 20 + [0] * 180
# O diagnóstico (presença do "pulo") foi positivo em 18 das 20 falhas e em 0 dos 180 sucessos
y_score = [1] * 18 + [0] * 2 + [0] * 180

# Cálculo da ROC e AUC
fpr, tpr, thresholds = roc_curve(y_true, y_score)
roc_auc = auc(fpr, tpr)

# Criando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='#2ecc71', lw=3, label=f'Sua Investigação (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='#e74c3c', lw=2, linestyle='--', label='Classificador Aleatório (Sorte)')

# Customização técnica
plt.xlim([-0.01, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos (Alarmes Falsos)')
plt.ylabel('Taxa de Verdadeiros Positivos (Sensibilidade)')
plt.title('A Incerteza Vira Certeza em uma Falha em VoIP')
plt.legend(loc="lower right")
plt.grid(True, linestyle='--', alpha=0.6)

# Salvando
plt.savefig('roc.jpg')
#plt.show()

print(f"AUC Calculado: {roc_auc}")
print(f"FPR: {fpr}")
print(f"TPR: {tpr}")