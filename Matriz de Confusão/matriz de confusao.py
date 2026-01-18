import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Para definir o negativo e o positivo, o scikit-learn considera as classes na ordem alfabética por padrão.
# Ou seja, uma matriz de confusão 2 x 2 é entendida pelo comando confusion_matrix() desta forma:
#  TN (modelo acertou a previsão de chamada NOK) | FP (modelo errou a previsão de chamada OK)
#  FN (modelo errou a previsão de chamada NOK) | TP (modelo acertou a previsão de chamada OK)
# Negativo = 'chamada NOK' | Positivo = 'chamada OK'
# Na caso atual, temos:
# TN = 3 | FP = 1
# FN = 0 | TP = 2
y_true = ['chamada NOK', 'chamada OK', 'chamada OK', 'chamada NOK', 'chamada NOK', 'chamada NOK']
y_pred = ['chamada NOK','chamada OK', 'chamada OK', 'chamada NOK', 'chamada OK', 'chamada NOK']
cm = confusion_matrix(y_true, y_pred)
print(cm)

print()
print('Testes pra ver se entendi a função sklearn.metrics.confusion_matrix().')
print('Quatro classes numéricas, de 0 a 3')
y_true = [3, 3, 0, 1, 1, 3, 3, 1, 1, 0, 0, 2, 2, 3, 2]
y_pred = [2, 3, 2, 1, 1, 3, 1, 2, 0, 0, 0, 2, 2, 1, 1]
cm = confusion_matrix(y_true, y_pred)
print('Minha matriz de confusão:', end=' ')
print('''
      [2 0 1 0]
      [1 2 1 0]
      [0 1 2 0]
      [0 2 1 2]
''')
print(cm)

print()
print('Classes categóricas: Churn, No Churn, Suspeito')
y_true = ['Churn', 'No Churn', 'Suspeito', 'Churn', 'Churn', 'No Churn', 'No Churn', 'No Churn', 'Suspeito', 'Suspeito', 'No Churn', 'Churn', 'Suspeito', 'Churn', 'No Churn']
y_pred = ['Churn', 'No Churn', 'No Churn', 'Churn', 'Churn', 'No Churn', 'Suspeito', 'No Churn', 'Suspeito', 'Suspeito', 'No Churn', 'Churn', 'Suspeito', 'No Churn', 'No Churn']
cm = confusion_matrix(y_true, y_pred)
print('Minha matriz de confusão:', end=' ')
print('''
      [4 1 0]
      [0 5 1]
      [0 1 3]
''')
print(cm)
