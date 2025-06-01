## Classificação de IMC

**Conjunto de Dados:**
[Dataset](https://github.com/gbhgit/tests/machine-learning-test/data.csv)

Features (X):
* Gender: Male / Female
* Height: Number (cm)
* Weight: Number (Kg)

Target (Y):
* Index (Classificação categórica do IMC)
  * 0: Extremely Weak
  * 1: Weak
  * 2: Normal
  * 3: Overweight
  * 4: Obesity
  * 5: Extreme Obesity

**Objetivo:**
Construir um modelo que classifique as categorias de IMC com base nas variáveis fornecidas.

---

## Instruções

Você deve criar uma solução que execute os seguintes 3 passos:


### **1. Pré-processamento dos Dados**

* Carregar os dados do arquivo CSV.
* Preparar os dados para o treinamento do modelo.

---

### **2. Treinar o Modelo de Classificação**

* Dividir o conjunto de dados em treino e teste (80/20).
* Salvar o modelo treinado em um arquivo.

---

### **3. Avaliação do Modelo**

* Avalie o modelo utilizando os dados de teste.
* Apresente a Matriz de Confusão**
* Apresente as seguintes métricas: acurácia, precision, recall, F1-score


## Observações

* Você pode utilizar as seguintes bibliotecas: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `joblib`, `pickle`.
* Use seu julgamento de como tratar o desbalanceamento.
