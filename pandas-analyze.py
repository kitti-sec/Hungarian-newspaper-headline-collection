import pandas as pd
import nltk
# nltk.download()  - enélkül nem mukodott a stopwords list amig felnem raktam minden komponenst
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

df=pd.read_csv('articles.csv')
tokenizedword = []

for i in df.Title:
    tokenizedword.append(word_tokenize(str(i)))

for i in df.Description:
    tokenizedword.append(word_tokenize(str(i)))


allWords = []
for wordList in tokenizedword:
    allWords += wordList

for i in range(len(allWords)):
    allWords[i] = allWords[i].lower()

# stop_words=set(stopwords.words("hungarian"))
stop_words = nltk.corpus.stopwords.words('hungarian')

custom_stopWorlds = [",",":","-","A","!","itt","miatt","is",'\"',]
stop_words.extend(custom_stopWorlds)

filtered_list = []
for w in allWords:
    if w not in stop_words:
        filtered_list.append(w)

fdist = FreqDist(filtered_list)
print(fdist)
print(fdist.most_common(10))

fdist.plot(30,cumulative=False)
plt.show()


