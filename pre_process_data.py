import nltk
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import joblib


nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
vectorizer = joblib.load('./static/vect_model.pkl')
model = joblib.load('./static/naive.pkl')


topic_list = ["CreditReport Or CreditBureus",
              "Fair Credit Reporting Act Violation",
              "CompromisedCreditReport Or UnauthorizedAccount",
              "Low Credit Score",
              "Loan Or Mortage Or Payment Issue",
              "IncorrectDataReport Or IdentityReport",
              "Unauthorized Use of Account Or FraudAccount",
              "Consumer Right Violation",
              "Identity Theft",
              "Credit Report Dispute"]


def re_clean(data):
    ex = re.sub("[^A-za-z\s]+" ,'',data)
    ex = re.sub("X",'',ex)
    ex = re.sub('\s+',' ',ex)
    ex = re.sub('\n','',ex)
    return ex.strip().lower()


def lemmatize(data):
    return ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(data) 
                        if word not in stop_words and len(word)> 2])

def tfidf(data):
    return vectorizer.transform([data])

def pred(data):
    topic = model.predict(data)[0]
    return topic_list[topic]

def main_fun(data):
    data = re_clean(data)
    data = lemmatize(data)
    data = tfidf(data)
    return pred(data)










