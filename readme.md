# Desafio Técnico: Previsão de Custos de Seguros de Saúde

## Descrição do Projeto

Este projeto é um desafio técnico cujo objetivo é identificar qual modelo de Regressão Linear é mais eficaz para prever os custos de seguros de saúde de uma pessoa, com base em atributos pessoais como ser fumante, número de filhos, IMC, região e idade.

## Colaboradores

Os modelos foram desenvolvidos por:

- **Daniel Felipe Klotz**  
  Email: [danielfelipeklotz@gmail.com](mailto:danielfelipeklotz@gmail.com)  
  RM: 358514

- **Felipe de Castro Sá Barreto**  
  Email: [febarretosk@gmail.com](mailto:febarretosk@gmail.com)  
  RM: 358703

- **Daniel Negreiros Cangianelli**  
  Email: [daniel.dw@live.com](mailto:daniel.dw@live.com)  
  RM: 359064

- **Henrique Sartal Santos**  
  Email: [rick.sartal@gmail.com](mailto:rick.sartal@gmail.com)  
  RM: 358617

## Detalhes do Conjunto de Dados

O conjunto de dados utilizado neste projeto está disponível no arquivo `us-insurance-data.csv`, obtido de [Kaggle](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset). Este dataset fornece uma visão abrangente sobre:

- **Idade**: Representa a idade do indivíduo em anos.
- **Sexo**: Indica o gênero do indivíduo, categorizado como masculino ou feminino.
- **IMC (Índice de Massa Corporal)**: Calculado como o peso em quilogramas dividido pelo quadrado da altura em metros, este índice avalia a relação entre peso e altura.
- **Filhos**: Número de dependentes que o indivíduo possui.
- **Fumante**: Um indicador binário que mostra se o indivíduo é fumante.
- **Região**: A área geográfica dos Estados Unidos onde o indivíduo reside, categorizada em nordeste, noroeste, sudeste e sudoeste.
- **Custos**: Refere-se aos custos anuais do seguro de saúde em dólares americanos.

## Modelos Desenvolvidos

### Regressão Linear

O notebook [`tech-challenge-linear-regression.ipynb`](tech-challenge-linear-regression.ipynb) contém a implementação de modelos de Regressão Linear. Este notebook explora diferentes abordagens e técnicas para otimizar a precisão das previsões de custos de seguros de saúde.

### Modelos Baseados em Árvores

O notebook [`tech-challenge-tree-based.ipynb`](tech-challenge-tree-based.ipynb) explora modelos baseados em árvores, como Árvores de Decisão e Florestas Aleatórias, para prever os custos de seguros de saúde. Estes modelos são comparados com os modelos de Regressão Linear para determinar qual abordagem oferece melhores resultados.

## Como Executar

1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o Python e o Jupyter Notebook instalados.
3. Abra os notebooks `tech-challenge-linear-regression.ipynb` e `tech-challenge-tree-based.ipynb` no Jupyter Notebook.
4. Execute as células para treinar os modelos e avaliar os resultados.

## Conclusão

Este projeto visa não apenas encontrar o melhor modelo de previsão, mas também fornecer insights sobre quais fatores mais influenciam os custos de seguros de saúde. Através da análise dos dados e do desenvolvimento de modelos preditivos, esperamos contribuir para uma melhor compreensão dos custos associados aos seguros de saúde.

O arquivo [`Relatório Tech Challenge Fase 01.pdf`](Relatório Tech Challenge Fase 01.pdf) descreve os passos e etapas exploratórias e analíticas desse projeto. 