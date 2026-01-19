import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# ---- Caso Embratel ----
# Chamadas reais:
# 20 chamadas falharam (classe negativa, 0)
# 180 chamadas tiveram sucesso (classe positiva, 1)
# Previsões:
# 18 chamadas falhas (classe negativa, 0)
# 182 chamadas com sucesso (classe positiva, 1)

y_real = [0] * 20 + [1] * 180 # lista com 200 classificações reais, sendo as 20 primeiras falhas e 180 sucessos
y_pred = [0] * 18 + [1] * 2 + [1] * 180  # lista com 200 previsões, sendo as 18 primeiras falhas (0) e 182 sucessos (1)

print(f'y_real:\n {y_real}')
print(f'y_pred:\n {y_pred}')
# Gerando a Matriz
cm = confusion_matrix(y_real, y_pred)
print(f'Confusion Matrix:\n 0 = Negativo = Falha, 1 = Positivo = Sucesso\n {cm}')

# Visualização
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues_r', 
            xticklabels=['Falha', 'Sucesso'], yticklabels=['Falha', 'Sucesso'])
plt.xlabel('Diagnóstico (Pulo no SDP)')
plt.ylabel('Realidade (Resultado VoIP)')
plt.title('Matriz de Confusão: Caso de Sucesso e Falha em VoIP')
plt.savefig('cm.jpg')
#plt.show()

print(classification_report(y_real, y_pred, target_names=['Falha', 'Sucesso']))

print('''
      Analisando a matriz de confusão acima:
      - de todas as previsões de falhas, o modelo acertou 100% (18 de 18): PRECISÃO de falha é 100%, 0% de FN!
      - de todas as falhas reais, apenas 2 FP ocorreram: SENSIBILIDADE (RECALL) da falha é 90% (18 de 20), 10% de FP!
      - acurácia geral do modelo: (18 + 180) / 200 = 99%, uma métrica alta, mas sem esquecer que o dataset é desbalanceado.
      
      CONCLUSÃO:
      O modelo é muito bom para prever falhas. A finalidade era o isolamento da causa raiz do problema intermitente de falhas
      em chamadas VoIP naquele laboratório de homologação da operadora.
    '''
      )