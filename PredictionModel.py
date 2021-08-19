import timeit
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import _pickle as pickle
import pickle 
import string
import nltk
import joblib
import re



start = timeit.default_timer()


with open("pickle/pipeline.pkl", 'rb') as f:
            model = pickle.load(f)
            stop = timeit.default_timer()
            print('=> Pickle Loaded in: ', stop - start)

class PredictionModel:
    output = {}

    def __init__(self, text):
        self.output['original'] = text

    def predict(self):
        review =self.preprocess()
        review=[review]
        self.output['prediction'] = 'fake' if model.predict(review)== 0 else 'real'
        return self.output


    # Helper methods
    def preprocess(self):
        sentence = self.output['original']
        filter_sentence =''
        stop_words = stopwords.words('english')
        lemmatizer=WordNetLemmatizer()
        sentence = re.sub(r'[^\w\s]','',sentence)
        words = nltk.word_tokenize(sentence) #tokenization
        words = [w for w in words if not w in stop_words]
        for word in words:
            filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
        return filter_sentence