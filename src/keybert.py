import pandas as pd
from .pre_processing import pre_process
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer


def bert_keywords():
    df = pd.read_excel("./reports/job_data.xlsx")
    # Pre-processing
    df['Description'] = df['Description'].astype(str)
    df['processed_descriptions'] = df['Description'] \
        .apply(lambda x:pre_process(x))

    # Get corpus
    document = df['processed_descriptions'].tolist()
    doc = ' '.join(document)

    sentence_model = SentenceTransformer(
        "distilbert-base-nli-mean-tokens", 
        device="cpu"
    )

    # KeyBERT with Sentence Transformer
    kw_model = KeyBERT(model=sentence_model)
    keywords = kw_model.extract_keywords(
        doc, 
        keyphrase_ngram_range=(1, 1), 
        stop_words="english", 
        top_n=30
    )

    bert_keywords_df = pd.DataFrame(
        keywords, 
        columns=["keyword", "score"]
    )

    return bert_keywords_df.to_excel("./reports/bert_keywords.xlsx",
                                    index=False)

bert_keywords()