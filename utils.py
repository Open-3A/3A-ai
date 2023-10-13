from typing import List
from pandas import DataFrame

def get_columns_from_header_0(multi_index_df: DataFrame) -> List[str]:
  return list(set([ticker for ticker, _ in multi_index_df.columns]))