from typing import List
import pandas as pd

def get_columns_from_header_0(multi_index_df: pd.DataFrame) -> List[str]:
  return list(set([ticker for ticker, _ in multi_index_df.columns]))

def get_tickers_from_market_index(source: str):
  market_index = pd.read_csv(source)
  market_index.drop(columns="Part. (%)", inplace=True)
  market_index.dropna(inplace=True)
  return market_index.iloc[:, 0].to_list()

def merge_tickers_from_market_indexes(*args: List[str]) -> List[str]:
  result = set()

  for market_index in args:
    result = result.union(market_index)

  return list(result)