import os
import pandas as pd

def load_raw_data():
    file_path = os.path.join(os.getcwd(), 'data', 'raw', 'retail.csv')
    df = pd.read_csv(file_path, encoding="latin1")
    return df

if __name__ == "__main__":
    df = load_raw_data()
    print(df.head(2))
    print(df.shape)
    print(df.info())