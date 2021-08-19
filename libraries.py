import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
import pip as sns
from.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from sklearn import linear_model
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.pipeline import Pipeline
import joblib


