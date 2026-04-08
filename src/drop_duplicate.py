import pandas as pd

def removerDuplicadas(data, coluna):
    df = pd.read_csv(data)
    df.drop_duplicates(subset=[coluna], keep='first', inplace=True)
    return df

if __name__ == "__main__":
    caminho = r'/home/joaoinacio/bootcamp-machine-learning/data/processed/dados_processed.csv'
    df = removerDuplicadas(caminho, 'img_hash')
    df.to_csv(r'/home/joaoinacio/bootcamp-machine-learning/data/processed/dataset_limpo_final.csv', index=False)
    print(f'Dataset criado com os seguinte tamanho {df.shape}')

