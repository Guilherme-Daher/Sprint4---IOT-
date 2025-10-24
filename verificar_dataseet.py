import os
from collections import Counter
 
# Caminho para a pasta do dataset
dataset_path = 'dataset'
 
# Lista todos os arquivos .jpg e extrai os IDs
ids = [f.split('.')[0] for f in os.listdir(dataset_path) if f.endswith('.jpg')]
contagem = Counter(ids)
 
# Mostra quantas imagens existem por ID
print("Imagens por ID:")
for id, qtd in contagem.items():
    print(f"ID {id}: {qtd} imagens")