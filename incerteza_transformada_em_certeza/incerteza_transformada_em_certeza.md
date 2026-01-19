# Estudo de Caso: Isolamento de Causa Raiz em Falhas VoIP
**Contexto:** Homologação de Produtos na Embratel

## 🎯 Objetivo
Identificar o fator determinante para falhas intermitentes no estabelecimento de chamadas em um laboratório de homologação técnica. O foco foi utilizar a **Matriz de Confusão** para validar estatisticamente uma hipótese de engenharia sobre o protocolo SDP.

---

## 🛠️ Metodologia e Resultados
Nesta análise, configurei a classe **Falha** como a **Classe Negativa (0)** e o **Sucesso** como a **Classe Positiva (1)**. A prioridade técnica foi garantir a confiabilidade do diagnóstico de falha para isolar a causa raiz.



### Principais Métricas de Performance:

* **Precisão da Classe Negativa (Falha): 100%**
    * O diagnóstico foi configurado para ser extremamente específico. Obter **zero Falsos Negativos (0% FN)** garantiu que toda vez que o modelo apontava uma falha, ela ocorria de fato na realidade. Isso permitiu confirmar o "pulo no protocolo SDP" como o fator causal direto.
* **Recall (Sensibilidade) da Classe Negativa: 90%**
    * O modelo foi capaz de explicar 90% de todas as falhas reais ocorridas no período. Os 10% restantes (2 casos de **Falsos Positivos**) indicam que, embora a causa principal tenha sido isolada, variáveis secundárias menores podem coexistir.
* **Acurácia Geral: 99%**
    * Apesar de elevada, a acurácia foi tratada como métrica secundária devido ao desbalanceamento do dataset (predomínio de sucessos), reforçando a necessidade de uma análise granular por classe.



---

## 💡 Conclusão Técnica
A aplicação de ferramentas de **Data Science** (Python, Scikit-Learn) permitiu transformar um problema intermitente de engenharia em um modelo estatístico validado. O isolamento com 100% de precisão na classe negativa confirmou a hipótese diagnóstica, reduzindo drasticamente o tempo médio de reparo (**MTTR**) e garantindo a certificação dos produtos VoIP junto à operadora.

---

### Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** Pandas, Scikit-Learn, Seaborn, Matplotlib
* **Conceitos:** Regressão Logística, Matrizes de Confusão, Métricas de Classificação