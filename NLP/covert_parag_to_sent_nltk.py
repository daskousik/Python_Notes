# The Natural Language Toolkit (NLTK)
import nltk
from nltk.stem import PorterStemmer  #
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

paragraph = '''Bali is predominantly a Hindu country. Bali is known for its elaborate, traditional dancing.
              The dancing is inspired by its Hindi beliefs. Most of the dancing portrays tales of good versus evil.
               To watch the dancing is a breathtaking experience. 
               Lombok has some impressive points of interest – the majestic Gunung Rinjani is an active volcano. 
               It is the second highest peak in Indonesia. Art is a Balinese passion.
                Batik paintings and carved statues make popular souvenirs.
                 Artists can be seen whittling and painting on the streets, particularly in Ubud. 
                 It is easy to appreciate each island as an attractive tourist destination. 
                 Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets 
                 every year. Snorkelling and diving around the nearby Gili Islands is magnificent. 
                 Marine fish, starfish, turtles and coral reef are present in abundance. 
                 Bali and Lombok are part of the Indonesian archipelago. Bali has some spectacular temples. 
                 The most significant is the Mother Temple, Besakih.
                  The inhabitants of Lombok are mostly Muslim with a Hindu minority. 
                  Lombok remains the most understated of the two islands. 
                  Lombok has several temples worthy of a visit, though they are less prolific.
                   Bali and Lombok are neighbouring islands.'''

sentence = nltk.sent_tokenize(paragraph) # (text: Any
print(sentence)

words = nltk.word_tokenize(paragraph)
print(words)

# Stemming
stemmer = PorterStemmer()
for i in range(len(sentence)):
    words = nltk.word_tokenize(sentence[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentence[i] = ' '.join(words)
print(sentence)

#=======================================================================================================================

#lemmatization

sentence2 = nltk.sent_tokenize(paragraph)

lemmatization = WordNetLemmatizer()

for i in range(len(sentence2)):
    words = nltk.word_tokenize(sentence2[i]) # (text: str
    words = [lemmatization.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentence2[i] = ' '.join(words)
print(sentence2)

# ==================================================================================================================
# Main sent : 'Bali is known for its elaborate, traditional dancing.'
# stem ----> bring neirby words not actual words or meaningfull. like , country -> countri, elaborate -> elabor, traditional dancing > tradit danc
# stem:   'bali known elabor , tradit danc .'
# lemmatization ---> bring actual words and meaningfull. like country -> country, elaborate -> elaborate, traditional dancing -> traditional dancing.
# lemma:  'Bali known elaborate , traditional dancing .'

# ===========================================================================================================================================
# Apply Bag Of Vector......
# Cleaning the text............
import re
corpus = []
sentence3 = nltk.sent_tokenize(paragraph)
for i in range(len(sentence3)):
    review = re.sub('[^a-zA-Z]', ' ', sentence3[i])
    review = review.lower()
    words = nltk.word_tokenize(review)
    words = [lemmatization.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    review = ' '.join(words)
    corpus.append(review)

print(corpus)

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
cv = CountVectorizer() # Use for Bag of
tfidfv = TfidfVectorizer()
X = cv.fit_transform(corpus).toarray()
X1 = tfidfv.fit_transform(corpus).toarray()
print(X)
print(X1)


