import pandas as pd
from preprocess import (word_tokenize,
                        get_stopwords,
                        get_unusual_words,
                        tokenizer)


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
