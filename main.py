from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import matplotlib.font_manager as fm

model = Word2Vec.load('word2vec.model')

plt.rcParams['font.family'] = ['Malgun Gothic', 'DejaVu Sans', 'Arial', 'sans-serif']

def show_similar_words_tsnescatterplot(model, word, size):
    arr = np.empty((0, size), dtype='f')
    arr = np.append(arr, np.array([model.wv[word]]), axis=0)
    plt_labels = [word]
    
    similar_words = model.wv.most_similar(word)
    for similar_word in similar_words:
        word_vector = model.wv[similar_word[0]]
        arr = np.append(arr, np.array([word_vector]), axis=0)
        plt_labels.append(similar_word[0])
    
    n_samples = arr.shape[0]
    perplexity = min(5, n_samples - 1)  # Ensure perplexity < n_samples
    tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity)
    np.set_printoptions(suppress=True)
    tsne_data = tsne.fit_transform(arr)
    
    X = tsne_data[:, 0]
    Y = tsne_data[:, 1]
    plt.scatter(X, Y)
    for label, x, y in zip(plt_labels, X, Y):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(X.min() + 0.00005, X.max() + 0.00005)
    plt.ylim(Y.min() + 0.00005, Y.max() + 0.00005)
    plt.show()

# Example usage
show_similar_words_tsnescatterplot(model, '강아지', 100)
