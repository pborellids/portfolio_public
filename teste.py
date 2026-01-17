import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Para definir o negativo e o posijjjjjjtivo, o scikit-learn considera as classes na ordem alfabética por padrão.
# Ou seja, uma matriz de confusão 2 x 2 é entendida pelo comando confusion_matrix() desta forma:
#  TN (modelo acertou a previsão de chamada NOK) | FP (modelo errou a previsão de chamada OK)
#  FN (modelo errou a previsão de chamada NOK) | TP (modelo acertou a previsão de chamada OK)
# Negativo = 'chamada NOK' | Positivo = 'chamada OK'
y_true = ['chamada NOK', 'chamada OK', 'chamada OK', 'chamada NOK', 'chamada NOK', 'chamada NOK']
y_pred = ['chamada NOK','chamada OK', 'chamada OK', 'chamada NOK', 'chamada OK', 'chamada NOK']
cm = confusion_matrix(y_true, y_pred)
print(cm)
