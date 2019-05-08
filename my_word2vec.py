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


default_model = gensim.models.Word2Vec.load('modelos/saved_models')
