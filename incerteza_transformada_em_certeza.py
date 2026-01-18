import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# 1 = Falha (Positivo), 0 = Sucesso (Negativo)
y_real = [1] * 20 + [0] * 180 # lista com 200 elementos, sendo os 20 primeiros com 1 e os 180 últimos com 0

# O diagnóstico detectou 18 das 20 falhas (90%) e nenhum falso positivo
y_pred = [1] * 18 + [0] * 2 + [0] * 180  # lista com 200 elementos, sendo os 18 primeiros com 1 e os próximos 180 com 0

print(f'y_real:\n {y_real}')
print(f'y_pred:\n {y_pred}')
# Gerando a Matriz
cm = confusion_matrix(y_real, y_pred)
print(f'Confusion Matrix:\n 1 = Positivo = Falha, 0 = Negativo = Sucesso\n {cm}')

# Visualização
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Sucesso', 'Falha'], yticklabels=['Sucesso', 'Falha'])
plt.xlabel('Diagnóstico (Pulo no SDP)')
plt.ylabel('Realidade (Resultado VoIP)')
plt.title('Matriz de Confusão: Caso de Sucesso e Falha em VoIP')
plt.savefig('cm.jpg')
#plt.show()

print(classification_report(y_real, y_pred, target_names=['Sucesso', 'Falha']))