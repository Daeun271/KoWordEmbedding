from gensim.models import Word2Vec
import os
import json

sentences = []

for i in range(10000, 9290000, 10000):
    file_name = f'wiki_{i}.json'
    file_path = os.path.join('wiki_morphs', file_name)
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            list = json.load(file)
            for morphs in list:
                sentences.append(morphs)
  
        print(f'{i} done')

model = Word2Vec(sentences=sentences, vector_size=100, window=5, min_count=5, workers=4, sg=1)
model.save('word2vec.model')