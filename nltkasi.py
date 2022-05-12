import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt


nltk.download('wordnet')

df = pd.read_csv(r'Resume_Data.csv', encoding = 'utf-8')
df['Cleaned_Resume'] = ''

print(df.head())

print("Resume Categories")
print(df['Category'].value_counts())

plt.figure(figsize = (10, 10))                                          # Setting size of plot
plt.xticks(rotation = 90)                                               # Rotating plot to organize horizontally
sns.countplot(y = 'Category', data = df)


def Clean_Resume(resumeText):
    Removals = [  # Deciding weeds in resume
        'http\S+\s*',  # Web URLs
        'RT|cc',  # Regular characters
        '#\S+',  # Hashtags
        '@\S+',  # Emails
        '\s+',
        ' â\S+'
    ]

    for weed in Removals: resumeText = re.sub(weed, ' ', resumeText)  # Removing weeds using regular expression
    # resumeText = re.sub('[%s]'%re.escape("""!"#$%&'_=-+()[];:,./?^*@{}|\~"""), ' ', resumeText)
    # resumeText = re.sub(r'[^x00-x7f]', r' ', resumeText)

    return resumeText

df['Cleaned_Resume'] = df.Resume.apply(lambda x: Clean_Resume(x))
df.head()

corpus = ''
for i in range(len(df)): corpus += df['Cleaned_Resume'][i]
corpus[450:1000]

tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(corpus)                                     # Tokenizing the text into individual words

words = [word.lower() for word in tokens]                               # Transforming all words to lowercase
print(len(words))

stopwords = nltk.corpus.stopwords.words('english')

words_new = [
    word
    for word in words
    if word not in stopwords
]

print(len(words_new))

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

lem_words = [
    wnl.lemmatize(word)
    for word in words_new
]

same=0
diff=0
for i in range(0,1832):
    if(lem_words[i]==words_new[i]):
        same=same+1
    elif(lem_words[i]!=words_new[i]):
        diff=diff+1
print('Number of words Lemmatized=', diff)
print('Number of words not Lemmatized=', same)

freq_dist = nltk.FreqDist(lem_words)
plt.subplots(figsize=(20,12))
freq_dist.plot(30)

mostcommon = freq_dist.most_common(50)
mostcommon

res=' '.join([i for i in lem_words if not i.isdigit()])

import os
os.system('pip install wordcloud')

plt.subplots(figsize=(16,10))
wordcloud = WordCloud(
                          background_color='black',
                          max_words=200,
                          width=1400,
                          height=1200
                         ).generate(res)
plt.imshow(wordcloud)
plt.title('Resume Text WordCloud (100 Words)')
plt.axis('off')
plt.show()

print(df.head())