# import nltk
# nltk.download('wordnet')

import re
from .non_essential_words import *
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()


def pre_process(text):
    
    # Remove special characters and digits
    text = re.sub("(\\d|\\W)+"," ",text)
    
    # Remove punctuations and numbers
    text = re.sub('[^a-zA-Z]', ' ', text)
    
    # lowercase
    text = text.lower()
    
    # Single character removal
    text = re.sub(r"\s+[a-zA-Z]\s+", ' ', text)

    # Removing multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    words = text.split()
    # Remove non-relevant words from job description
    meaningful_words = [w for w in words if not w in non_essential_words]

    # Lemmatization reduces the inflected words properly ensuring that 
    # the root word belongs to the language
    lemmatized_words = [wordnet_lemmatizer.lemmatize(w) for w in meaningful_words]
    return(" ".join(lemmatized_words))