Sistema de Recomendação de Filmes - MovieLens
Este projeto implementa um sistema de recomendação de filmes baseado nos dados do MovieLens, utilizando MongoDB para armazenamento e Python para análise e modelagem de dados.

Visão Geral
O objetivo é explorar a base de dados MovieLens, identificar padrões de comportamento dos usuários e construir modelos de aprendizado de máquina que possam prever as preferências dos usuários.

Estrutura do Projeto
plaintext
Copiar código
project/
├── load_data.py           # Script para carregar os dados no MongoDB
├── exploration.py         # Código para análise exploratória dos dados
├── models.py              # Código para construção e avaliação dos modelos
├── movies.csv             # Dados de filmes (MovieLens)
├── ratings.csv            # Dados de avaliações (MovieLens)
├── README.md              # Documentação do projeto
Pré-requisitos
Certifique-se de ter os seguintes softwares instalados:

Python 3.8+
MongoDB Community Edition
Pacotes Python necessários (instalados com pip install -r requirements.txt).
Requisitos Python
Crie um arquivo requirements.txt com os seguintes pacotes:

plaintext
Copiar código
pandas
pymongo
scikit-learn
tensorflow
numpy
matplotlib
seaborn
Para instalar:

bash
Copiar código
pip install -r requirements.txt
Configuração e Execução
1. Configurar o MongoDB
Certifique-se de que o MongoDB está rodando localmente em localhost:27017.
Inicie o servidor:
bash
Copiar código
net start MongoDB  # Windows
sudo systemctl start mongod  # Linux/Mac
2. Carregar os Dados
Execute o script load_data.py para carregar os dados do MovieLens no MongoDB:
bash
Copiar código
python load_data.py
3. Análise Exploratória
Use o script exploration.py para realizar análises exploratórias dos dados, como:
Distribuição de ratings.
Preferências de gênero.
Identificação de padrões e outliers.
bash
Copiar código
python exploration.py
4. Construção de Modelos
Execute o script models.py para treinar e avaliar diferentes modelos de aprendizado de máquina:
Árvore de Decisão
Rede Neural
Naive Bayes
bash
Copiar código
python models.py
Principais Funcionalidades
1. Exploração de Dados
Visualizações para entender os dados de usuários e filmes.
Análise de correlação entre gêneros, ratings e comportamento do usuário.
2. Modelagem Preditiva
Árvore de Decisão: Classificação de ratings como altos ou baixos.
Rede Neural: Previsão do rating exato com base no histórico do usuário e características do filme.
Naive Bayes: Predição binária (gostar ou não de um filme) com base em dados categóricos.
3. Comparação de Modelos
Avaliação do desempenho dos modelos usando métricas como:
Acurácia
F1-score
RMSE
Resultados Esperados
Relatórios:

Gráficos e insights da análise exploratória.
Comparações de métricas de desempenho entre os modelos.
Sistema de Recomendação:

Sugestões de filmes personalizadas para cada usuário, com base nos modelos treinados.
Contribuição
Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões, envie um pull request ou abra uma issue.

Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Referências
Dataset MovieLens
Documentação do MongoDB
Orange Data Mining
