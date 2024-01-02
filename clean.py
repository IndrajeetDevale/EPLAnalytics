import pandas as pd

def read_csv(file):
    return pd.read_csv(file, encoding='ISO-8859-1')

def main():
    df = read_csv('results.csv')
    print(df)

if __name__ == '__main__':
    main()