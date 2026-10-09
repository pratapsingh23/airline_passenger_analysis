import pandas as pd

'---------------------------------------------------'
# Importing Dataset:
'---------------------------------------------------'

# Path of Dataset:
dataset_path = '/content/drive/MyDrive/data.csv'

'---------------------------------------------------'
# Function for loading dataset:
def get_dataset(path: str) -> pd.DataFrame | None:
  """
  Returns the Dataframe or None from path.
  """
  try:
    return pd.read_csv(path)
  except FileNotFoundError:
    print('Dataset file Not Found!')
    return None
  except Exception as e:
    print(f"Error occur: {e}")
    return None

'---------------------------------------------------'
# Checking if df is None or not:
if __name__ == '__main__':
  df = get_dataset(dataset_path)
  if df is None:
    raise ValueError('Dataset not loaded!')
  else:
    print("Dataset loaded.")

