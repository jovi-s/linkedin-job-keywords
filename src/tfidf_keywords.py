import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from .pre_processing import pre_process


def keyword_weights():
    df = pd.read_excel("./reports/job_data.xlsx")
    # Pre-processing
    df['Description'] = df['Description'].astype(str)
    df['processed_descriptions'] = df['Description'].apply(lambda x:pre_process(x))

    # Get corpus
    descriptions = df['processed_descriptions'].tolist()

    vectorizer = TfidfVectorizer(stop_words='english', 
                                max_features=30)
    X = vectorizer.fit_transform(descriptions)

    df_idf = pd.DataFrame(vectorizer.idf_, 
                        index=vectorizer.get_feature_names(), #.vocabulary_
                        columns=["idf_weights"])

    df_idf = df_idf.sort_values(by=['idf_weights'], ascending=False)
    return df_idf.to_excel("./reports/top_tfidf_keywords.xlsx")