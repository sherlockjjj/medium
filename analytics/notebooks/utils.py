import pandas as pd
import spacy

nlp = spacy.load('en')


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


def word_count(x):
    """
    count the number of words
    """
    return pd.DataFrame(
        {'{}_wc'.format(x.name): x.apply(lambda text: len(text.split(' ')))})

