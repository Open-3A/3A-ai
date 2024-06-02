# Modelo de Fluxo de Caixa Descontado

## Introdução

O objetivo deste projeto é desenvolver um modelo para estimar o preço teto de ativos listados na bolsa de valores
utilizando o Modelo de Gordon, também conhecido como Modelo de Crescimento de Dividendos. Este modelo é uma ferramenta
essencial para investidores, pois permite a avaliação do valor intrínseco de uma ação baseada nos dividendos futuros
esperados e na taxa de retorno exigida.

## Metodologia

### 1. Coleta de Dados

Para a análise, utilizamos a biblioteca `yfinance` para coletar dados históricos de dividendos de empresas listadas no
Índice de Dividendos da Bolsa de Valores Brasileira. Os dados foram consolidados em um DataFrame, facilitando o
processamento subsequente.

### 2. Classificação dos Ativos

Os ativos foram classificados com base nos valores totais dos dividendos pagos. Utilizamos o algoritmo de agrupamento
K-means, um método de aprendizado não supervisionado, para dividir os ativos em três categorias distintas:

- Dividendos Baixos
- Dividendos Moderados
- Dividendos Altos

A normalização dos dados foi feita utilizando o `StandardScaler` para garantir que os dados estivessem na mesma escala,
o que é crucial para a performance do algoritmo de agrupamento.

### 3. Previsão de Dividendos

Para prever os dividendos futuros, empregamos o algoritmo Prophet, um modelo de séries temporais desenvolvido pelo
Facebook. Treinamos modelos de séries temporais específicos para cada categoria de dividendos identificada. As previsões
de dividendos são fundamentais para o cálculo do valor intrínseco dos ativos futuros.

### 4. Cálculo do Valor Intrínseco

Utilizando o Modelo de Gordon, calculamos o valor intrínseco das ações. Este modelo se baseia na fórmula:

$$ P = \frac{D_1}{r - g} $$

Onde:

- $P$ = Valor intrínseco da empresa;
- $D_1$ = Valor esperado dos dividendos no próximo ano;
- $r$ = Taxa de retorno exigida (usamos o Return on Invested Capital - ROIC);
- $g$ = Taxa de crescimento dos dividendos.

O ROIC atual e médio das empresas foram obtidos de fontes externas utilizando automação de coleta de dados com Selenium.

## Resultados

### Classificação dos Ativos

Os ativos foram classificados em três categorias distintas baseadas nos dividendos pagos. Esta classificação facilita a
análise de padrões de pagamento de dividendos entre empresas e permite o agrupamento de empresas com perfis de pagamento
de dividendos semelhantes.

### Previsão de Dividendos

Os modelos Prophet forneceram previsões de dividendos para os próximos anos. Essas previsões foram ajustadas para
garantir que valores negativos de dividendos não fossem considerados, melhorando a precisão das estimativas.

### Valor Intrínseco

O valor intrínseco das ações foi calculado considerando as previsões de dividendos e o ROIC das empresas. Este cálculo é
essencial para determinar o preço teto de uma ação, ajudando os investidores a identificar se uma ação está
subvalorizada ou supervalorizada.

## Limitações

1. **Premissas do Modelo de Gordon**: O modelo assume que os dividendos crescerão a uma taxa constante indefinidamente,
   o que pode não ser realista para todas as empresas.
2. **Qualidade dos Dados**: A precisão das previsões depende da qualidade e completude dos dados históricos de
   dividendos. Dados faltantes ou imprecisos podem afetar a qualidade das previsões.
3. **Variabilidade do ROIC**: O ROIC pode variar significativamente ao longo do tempo, e usar um valor médio pode não
   capturar adequadamente essa variabilidade.

## Próximos Passos

1. **Aprimoramento das Previsões**: Explorar outros modelos de previsão de séries temporais que possam capturar melhor a
   variabilidade dos dividendos.
2. **Análise de Sensibilidade**: Realizar análises de sensibilidade para entender como mudanças nas taxas de crescimento
   de dividendos e no ROIC afetam o valor intrínseco das ações.
3. **Expansão do Modelo**: Aplicar o modelo a um conjunto maior de empresas e verificar sua aplicabilidade em diferentes
   setores e mercados.
4. **Incorporação de Fatores Adicionais**: Considerar outros fatores financeiros e econômicos que possam influenciar os
   dividendos e o valor intrínseco das ações.

## Anexos

- [brazilian_companies_cashflow.ipynb](../brazilian_companies_cashflow.ipynb) - Contém a análise de fluxo de caixa das empresas brasileiras.
- [future-cash-flow-model.ipynb](../future-cash-flow-model.ipynb) - Implementação do modelo de previsão de fluxo de caixa futuro.
- [predict_cash_flow_components.ipynb](../predict_cash_flow_components.ipynb) - Previsão dos componentes do fluxo de caixa.

Estes arquivos detalham a implementação prática dos conceitos discutidos no relatório e são fundamentais para a
reprodução e verificação dos resultados apresentados.