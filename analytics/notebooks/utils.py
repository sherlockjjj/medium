import nltk
import pandas as pd


def parse_date(x):
    """
    parse date into year, month, day
    """
    return pd.DataFrame(
        {
            'year': x.dt.year,
            'month': x.dt.month,
            'day': x.dt.day
        }
    )


def tokenizer(text):
    """
    convert a string to list of string
    """
    return nltk.tokenize.word_tokenize(text)


def get_stopwords(tokens):
    """
    get stopword tokens
    """
    stopwords = nltk.corpus.stopwords.words('english')
    return [t for t in tokens if t.lower() in stopwords]


def filter_stopwords(tokens):
    """
    drop stopword tokens
    """
    stopwords = nltk.corpus.stopwords.words('english')
    return [t for t in tokens if t.lower() not in stopwords]


def get_unusual_words(tokens):
    """
    get unusual word tokens
    """
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    return [t for t in tokens if t.lower() not in english_vocab]


def filter_unusual_words(tokens):
    """
    drop unusual word tokens
    """
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    return [t for t in tokens if t.lower() in english_vocab]


def word_tokenize(text):
    """
    convert a string to list of normal word tokens
    """
    return filter_unusual_words(filter_stopwords(tokenizer(text)))


def get_word_count(x):
    """
    return normal word count, stop word count, unusual word count
    """
    wc = x.apply(lambda text: len(word_tokenize(text)))
    stop_wc = x.apply(lambda text: len(get_stopwords(tokenizer(text))))
    unusual_wc = x.apply(lambda text: len(get_unusual_words(tokenizer(text))))
    return pd.DataFrame(
        {
            '{}_word_count'.format(x.name): wc,
            '{}_stopword_count'.format(x.name): stop_wc,
            '{}_unusual_word_count'.format(x.name): unusual_wc,
            '{}_total_word_count'.format(x.name): wc + stop_wc + unusual_wc
        }
    )
