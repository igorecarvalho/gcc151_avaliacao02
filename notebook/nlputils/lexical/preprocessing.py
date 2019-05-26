import nltk
import unidecode
import string
import re

REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

#from nltk.corpus import stopwords
#stop_words = stopwords.words('portuguese')

class Preprocessing:

    def __init__(self):
        self.sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
        self.stemmer = nltk.stem.RSLPStemmer()
    #remove os acentos
    def remove_accents(self, text):
        return unidecode.unidecode(text)
    # remove a pontuacao
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('','',string.punctuation))
    #sentencia o texto
    def tokenize_sentences(self, text):
        sentences = self.sent_tokenizer.tokenize(text)
        return sentences
    #tokeniza o texto
    def tokenize_words(self, text):
        tokens = nltk.tokenize.word_tokenize(text)
        return tokens
    #coloca todas as palavras em minuscula
    def lowercase(self, text):
        return text.lower()
