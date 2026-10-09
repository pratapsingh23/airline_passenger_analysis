import pandas as pd
from IPython.display import display

"--------------------------------------------------------"
# Data Inspecting:
"--------------------------------------------------------"
def show_summary(df: pd.DataFrame)-> None:

  """
  Display a clean and readable data from dataframe.
  """

  print('Shape: ', df.shape)

  print("\nData Types: ")
  display(df.dtypes.to_frame("Types"))

  print("\nMissing values: ")
  display(df.isnull().sum().to_frame("Missing values"))

  print("\nDuplicates: ", df.duplicated().sum())

"--------------------------------------------------------"
