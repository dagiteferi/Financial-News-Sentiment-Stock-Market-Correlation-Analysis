import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def clean_headlines(data):
    data['clean_headline'] = data['headline'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x.lower()))
    stop_words = set(stopwords.words('english'))
    data['tokens'] = data['clean_headline'].apply(lambda x: [word for word in word_tokenize(x) if word not in stop_words])
    data['cleaned_text'] = data['tokens'].apply(lambda x: ' '.join(x))
    return data

def get_common_words(data, n=10):
    all_text = ' '.join(data['cleaned_text'].tolist())
    words = re.findall(r'\b\w+\b', all_text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

def word_frequency_over_years(data, top_words):
    word_freq_per_year = {word: [] for word in top_words}
    years = sorted(data['year'].unique())

    for year in years:
        yearly_text = ' '.join(data[data['year'] == year]['cleaned_text'].tolist())
        yearly_words = re.findall(r'\b\w+\b', yearly_text.lower())
        yearly_word_counts = Counter(yearly_words)
        for word in top_words:
            word_freq_per_year[word].append(yearly_word_counts[word])

    return years, word_freq_per_year