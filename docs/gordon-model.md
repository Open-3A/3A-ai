# Modelo de Gordon

## Introdução
O objetivo deste projeto é desenvolver um modelo que estime o preço teto de ativos listados na bolsa de valores utilizando o Modelo de Gordon, também conhecido como Modelo de Crescimento de Dividendos. Este modelo é amplamente utilizado na avaliação de ações e se baseia na premissa de que os dividendos crescerão a uma taxa constante indefinidamente. A estimativa de preço teto é crucial para investidores que buscam identificar o valor intrínseco de uma ação e tomar decisões de investimento informadas.

## Metodologia

### 1. Coleta de Dados
Para realizar a análise, coletamos dados históricos de dividendos das empresas listadas em um índice específico do mercado. Utilizamos a biblioteca `yfinance` para obter esses dados e armazená-los em um DataFrame para posterior processamento.

### 2. Classificação dos Ativos
A classificação dos ativos foi realizada com base nos valores totais dos dividendos pagos. Para isso, aplicamos o algoritmo de agrupamento K-means, que nos permitiu dividir os ativos em três categorias distintas: Dividendos Baixos, Moderados e Altos. A normalização dos dados foi feita utilizando o `StandardScaler` para garantir que os dados estivessem na mesma escala.

### 3. Previsão de Dividendos
Para prever os dividendos futuros, utilizamos o algoritmo Prophet, um modelo de séries temporais desenvolvido pelo Facebook. Treinamos modelos de séries temporais para cada categoria de dividendos identificada anteriormente. Essas previsões são fundamentais para calcular o valor intrínseco dos ativos no futuro.

### 4. Cálculo do Valor Intrínseco
O valor intrínseco das ações foi calculado utilizando o Modelo de Gordon. Este cálculo envolveu a utilização das previsões de dividendos e do Return on Invested Capital (ROIC) atual e médio das empresas. O ROIC foi obtido de fontes externas utilizando a biblioteca Selenium para automação de coleta de dados na web.

## Resultados

### Classificação dos Ativos
Os ativos foram classificados em três categorias baseadas nos dividendos pagos. Esta classificação ajuda a entender o comportamento de pagamento de dividendos das empresas e agrupar empresas com perfis semelhantes.

### Previsão de Dividendos
Os modelos Prophet fornecem previsões de dividendos para os próximos anos. Essas previsões são cruciais para aplicar o Modelo de Gordon e estimar o valor intrínseco das ações. As previsões foram ajustadas para garantir que valores negativos de dividendos não fossem considerados.

### Valor Intrínseco
O valor intrínseco das ações foi calculado considerando as previsões de dividendos e o ROIC das empresas. Este valor intrínseco é essencial para determinar o preço teto de uma ação, ajudando investidores a identificar se uma ação está subvalorizada ou supervalorizada.

## Limitações

1. **Premissas do Modelo de Gordon**: O Modelo de Gordon assume que os dividendos crescerão a uma taxa constante indefinidamente, o que pode não ser realista para todas as empresas.
2. **Dados Históricos**: A qualidade das previsões de dividendos depende da precisão e da completude dos dados históricos de dividendos. Dados faltantes ou imprecisos podem afetar a qualidade das previsões.
3. **ROIC Variável**: O ROIC pode variar significativamente ao longo do tempo, e usar um valor médio pode não capturar adequadamente essa variabilidade.

## Próximos Passos

1. **Aprimoramento das Previsões**: Explorar outros modelos de previsão de séries temporais que possam capturar melhor a variabilidade dos dividendos.
2. **Análise de Sensibilidade**: Realizar análises de sensibilidade para entender como mudanças nas taxas de crescimento de dividendos e no ROIC afetam o valor intrínseco das ações.
3. **Expansão do Modelo**: Aplicar o modelo a um conjunto maior de empresas e verificar sua aplicabilidade em diferentes setores e mercados.
4. **Incorporação de Fatores Adicionais**: Considerar outros fatores financeiros e econômicos que possam influenciar os dividendos e o valor intrínseco das ações.

## Anexos

- [gordon_model.ipynb](../gordon_model.ipynb)
- [dividend-prediction.ipynb](../dividend-prediction.ipynb)

Estes arquivos detalham a implementação prática dos conceitos discutidos no relatório e são fundamentais para a
reprodução e verificação dos resultados apresentados.