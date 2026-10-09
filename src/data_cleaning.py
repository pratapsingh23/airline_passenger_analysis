import pandas as pd

"--------------------------------------------------------"
# Column name change:
"--------------------------------------------------------"
def change_column_name(df: pd.DataFrame) -> pd.DataFrame:

  """
  Return a copy of dataframe with clear column name:
  lower case, no extra space, replace '-' to ' '.
  """
  df = df.copy()
  df.columns = (
      df.columns.
      str.strip().
      str.lower().
      str.replace(r"[ /-]", "_", regex=True)
  )

  return df
"--------------------------------------------------------"


