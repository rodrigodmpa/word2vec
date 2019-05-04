import gensim
import os
from nltk.stem.snowball import SnowballStemmer
stm = SnowballStemmer("portuguese")
import warnings
warnings.filterwarnings("ignore")
import glob

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for dirName in os.listdir(self.dirname):
            #print(dirName)
            for fname in os.listdir(os.path.join(self.dirname, dirName)):
                pathAux = os.path.join(self.dirname, dirName)
                for line in open(pathAux +'/'+ fname):
                    #print(line)
                    yield line.split()

# articles = MySentences('../modelo_salvo/data/')
# model = gensim.models.Word2Vec(articles, min_count=10, size=100, workers=-1)
# model.save('saved_models')

default_model = gensim.models.Word2Vec.load('modelos/saved_models')

# default_model.wv.similarity('leis','decreto')
# default_model.wv.similarity('bicicleta','roda')
# default_model.wv.most_similar_to_given('alface', ['freio', 'couve','folha','verde'])
# default_model.wv.most_similar(positive=['mulher','advogado'], negative=['homem'], topn=1)
# default_model.wv.similar_by_word("homem")
# default_model.wv.distance("carro", "roda")
# default_model.wv.n_similarity(["guitarra", "baixo"], ["musica", "banda"])
# default_model['politica']