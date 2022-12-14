# -*- coding: utf-8 -*-
"""Analysis_GP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11KMTJOpoI-OF7sj5rGJP_r-N0wKGCp0s

#Importing the required libraries
"""

import pandas as pd # import pandas library and alias it as pd
import numpy as np # import numpy library and alias it as np
import regex as re # import regex library and alias it as re
from collections import Counter # import Counter class from collections module
import glob # import glob module
import os # import os module
import re # import regular expression module
from tqdm.notebook import trange, tqdm # import trange and tqdm functions from tqdm.notebook module

"""#Extracting the male and female counts"""

#Define the preprocessingCSV() function, which performs the preprocessing steps on the text data
def preprocessingCSV(df):
  # call the "articlePreprocessing" function and pass the dataframe as input
  articlePreprocessing(df)
  #Count the occurrences of male and female pronouns in the text using regular expressions
  male_count = pronounCount(df, r'\b(he|his|him)\b')
  female_count = pronounCount(df, r'\b(she|her|hers)\b')
  #Return the male and female pronoun counts
  return male_count, female_count

"""#Article Preprocessing

"""

# define a function named "articlePreprocessing" that takes in a dataframe as input
def articlePreprocessing(df):
  # convert all the text in the "Text" column of the dataframe to lowercase
  df['Text'] = df['Text'].str.lower()
  # remove leading and trailing whitespaces from the text in the "Text" column of the dataframe
  df['Text'].str.strip()
  # convert all the values in the "Text" column of the dataframe to string data type
  df['Text'] = df['Text'].apply(str)

"""#Getting the male, female pronoun count"""

#Define the pronounCount() function, which counts the occurrences of pronouns in the text data using a regular expression
def pronounCount(df, regex_match_str):
  #Compile the regular expression pattern
  pronounRegex = re.compile(regex_match_str,re.I)
  count = 0
  #Loop through each row of the DataFrame and find all occurrences of the pronoun in the text
  for i in trange(len(df)):
    pronouns = pronounRegex.findall(df['Text'][i])
    #Add up the total number of pronouns found for all rows
    count += len(pronouns)
  #Return the total pronoun count
  return count

def ratio(Mcount, Fcount):
  return Fcount / (Fcount + Mcount) * 100

"""# Processing"""

path = "/content/drive/MyDrive/ADS-1/1800's data"
dirs = os.listdir(path)

count_dict = {}
#Loop through each text file in the data directory, excluding the "articles.csv" file, and perform the following preprocessing steps
for dir in dirs:
  # do not consider articles.csv
  if dir != 'articles.csv':
    #Read the text file as a pandas DataFrame
    df = pd.read_csv(os.path.join(path, dir), low_memory=True, delimiter=';')
    #Extract the year from the file name
    year = dir.split("_")[-1][:-4]
    #Apply preprocessing to the text data to clean and prepare it for analysis
    male_count, female_count = preprocessingCSV(df)
    #Save the count results for each year in a dictionary
    count_dict[year] = {'male_count': male_count, 'female_count': female_count}

count_dict #Print count_dict

# create a list of years from 1800 to 2008
years = list(range(1800, 2008))
# convert the list of years to a tuple
years = tuple(years)
# initialize an empty list to store male pronoun counts
male_count = []
# initialize an empty list to store female pronoun counts
female_count = []
# iterate over the tuple of years
for year in years: 
  # check if the current year exists as a key in the "count_dict" dictionary
  if str(year) in count_dict.keys(): 
    # append the male pronoun count for the current year to the "male_count" list
    male_count.append(count_dict[str(year)]['male_count']) 
    # append the female pronoun count for the current year to the "female_count" list
    female_count.append(count_dict[str(year)]['female_count']) 
    # if the current year does not exist in the "count_dict" dictionary
  else: 
    # append a null value to the "male_count" list
    male_count.append(None) 
    # append a null value to the "female_count" list
    female_count.append(None)

#Printing the length of male count and female count
print(len(male_count))
print(len(female_count))

from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [35.50, 15.50]

# Set the font size for the axes labels and tick labels
plt.rcParams.update({'font.size': 18})

# Add a title
plt.title('Pronoun Usage Over Time')

# Set the x-axis label
plt.xlabel('Years')

# Set the y-axis label
plt.ylabel('Pronoun count')

# Set the tick locations and labels for the x-axis
#plt.xticks(years, years, rotation=90)

# Use aesthetically pleasing colors for the lines
line1, = plt.plot(years, male_count, label="Male Pronoun Count", color='#1f77b4', linewidth=5)
line2, = plt.plot(years, female_count, label="Female Pronoun Count", color='#e377c2', linewidth=5)

# Add a legend
leg = plt.legend(loc='upper center')

# Don't show the grid
plt.grid(False)

# Show the plot
plt.show()

from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [35.50, 15.50]

# Set the font size for the axes labels and tick labels
plt.rcParams.update({'font.size': 18})

# Add a title
plt.title('Male Pronoun Usage Over Time')

# Set the x-axis label
plt.xlabel('Years')

# Set the y-axis label
plt.ylabel('Male Pronoun count')

# Set the tick locations and labels for the x-axis
#plt.xticks(years, years, rotation=90)

# Use aesthetically pleasing colors for the lines
line1, = plt.plot(years, male_count, color='#1f77b4', linewidth=5)

# Add a legend
leg = plt.legend(loc='upper center')

# Don't show the grid
plt.grid(False)

# Show the plot
plt.show()

from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [35.50, 15.50]

# Set the font size for the axes labels and tick labels
plt.rcParams.update({'font.size': 18})

# Add a title
plt.title('Female Pronoun Usage Over Time')

# Set the x-axis label
plt.xlabel('Years')

# Set the y-axis label
plt.ylabel('Female Pronoun count')

# Set the tick locations and labels for the x-axis
#plt.xticks(years, years, rotation=90)

# Use aesthetically pleasing colors for the lines
line1, = plt.plot(years, female_count, color='#e377c2', linewidth=5)

# Add a legend
leg = plt.legend(loc='upper center')

# Don't show the grid
plt.grid(False)

# Show the plot
plt.show()

"""#Reading the 1925's CSV File


"""

#Reading the CSV file
df = pd.read_csv("/content/drive/MyDrive/ADS-1/1800's data/parliament_articles_1925.csv", low_memory = True, delimiter = ';')

#Printing the first 20 rows of the data
df.head(20)

"""#Checking if the Text Column has any null values"""

#Checking if the text column has any null values
df['Text'].isnull().values.any()

#Checking the number of null values in the Text column
df['Text'].isnull().sum()

#checking the number of rows and columns of the dataset
df.shape

"""#Replacing the Null values with 'No TEXT Available'"""

#Filling the null columns with "No Text available"
df['Text'].fillna("No Text Available", inplace = True)

#Rechecking if the text column has any null values after filling the null columns with "No text available"
df['Text'].isnull().values.any()

"""#Word2Vec"""

# Import the gensim library
import gensim

# Import sample text and get temporary file path
from gensim.test.utils import common_texts, get_tmpfile

# Import the Word2Vec model
from gensim.models import Word2Vec

# Get the "Text" column from the dataframe as a list of tokenized words
articles_text = df.Text.apply(gensim.utils.simple_preprocess)

# Print the tokenized words
articles_text

"""This code imports the Word2Vec class from the gensim.models.word2vec module and then creates a Word2Vec model with a window size of 10 and a minimum count of 2. The window size is the maximum distance between the target word and its neighboring words, and the minimum count is the minimum number of occurrences of a word in the corpus for it to be included in the model. These parameters can be adjusted to change the behavior of the model and to improve its performance on a specific dataset."""

# Import the Word2Vec class from the gensim.models.word2vec module
from gensim.models.word2vec import Word2Vec

# Create a Word2Vec model with a window size of 10 and a minimum count of 2
model = gensim.models.Word2Vec(window=10, min_count=2)

"""The code is calling the build_vocab() method of a Word2Vec model to build a vocabulary from the given list of text articles. The progress_per parameter specifies the number of articles to process before displaying a progress update. This can be useful when working with large datasets to monitor the progress of the vocabulary building process.

The build_vocab() method processes the text articles to extract the unique words and their frequencies. These words and frequencies are used to create the vocabulary for the model, which is a list of the most common words in the corpus and their corresponding word vectors. The vocabulary is an important part of the model and is used for training, prediction, and other tasks.

Once the vocabulary is built, the model can be trained on the text data to learn the relationships between words and their vectors. This will allow the model to perform tasks such as finding the nearest neighbors of a given word or predicting the next word in a sequence.
"""

model.build_vocab(articles_text, progress_per = 1000)

"""The epochs attribute of a Word2Vec model specifies the number of times the model has been trained on the data. This value is set when the model is initialized and can be modified using the train() method. In general, training the model for more epochs can improve its performance, but it can also increase the training time and may result in overfitting."""

# access the "epochs" attribute of the "model" object
model.epochs

# Call the train() method of the Word2Vec model to train the model on the list of text articles.
# The total_examples parameter specifies the total number of examples in the training data.
# The epochs parameter specifies the number of training epochs to perform.
model.train(articles_text, total_examples=model.corpus_count, epochs=model.epochs)

# save the Word2Vec model to the file "savedmodel.model" in the current directory
model.save("./savedmodel.model")

"""The code is calling the most_similar() method of the Word2Vec model's wv attribute to find the words that are most similar to the given input word. This method returns a list of tuples, each containing a word and its similarity score to the input word. The list is sorted by similarity score in descending order, so the most similar words will appear at the top of the list."""

#Checking the similar words to woman
model.wv.most_similar("woman")

model.wv.most_similar("her")

model.wv.most_similar("she")

model.wv.most_similar("man")

model.wv.most_similar("him")

model.wv.most_similar("he")

#Checking the similarity between the words man and patience
model.wv.similarity(w1 = "man", w2 = "patience")

model.wv.similarity(w1 = "woman", w2 = "patience")

model.wv.similarity(w1 = "man", w2 = "goodness")

model.wv.similarity(w1 = "woman", w2 = "goodness")

import pandas as pd
import numpy as np
import re
from tqdm import tqdm
  
from gensim.models.fasttext import FastText
 
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt
 
# Lemmatization
from nltk.stem import WordNetLemmatizer
stemmer = WordNetLemmatizer()

df = pd.read_csv("/content/drive/MyDrive/ADS-1/1800's data/parliament_articles_1928.csv", low_memory = True, delimiter = ';')
print('List of all columns')
print(list(df))
 
# Checking for missing values in our dataframe
# No there is no missing value
df.isnull().sum()

df['Text'].fillna("No Text Available", inplace = True)

# Subset data for gensim fastText model
all_sent = list(df['Text'])
some_sent = all_sent[0:100000]

import nltk
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
# Text cleaning function for gensim fastText word embeddings in python
def process_text(document):
     
            # Remove extra white space from text
        document = re.sub(r'\s+', ' ', document, flags=re.I)
         
        # Remove all the special characters from text
        document = re.sub(r'\W', ' ', str(document))
 
        # Remove all single characters from text
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
 
        # Converting to Lowercase
        document = document.lower()
 
        # Word tokenization       
        tokens = document.split()
        # Lemmatization using NLTK
        lemma_txt = [stemmer.lemmatize(word) for word in tokens]
        # Remove stop words
        lemma_no_stop_txt = [word for word in lemma_txt if word not in en_stop]
        # Drop words 
        tokens = [word for word in tokens if len(word) > 3]
                 
        clean_txt = ' '.join(lemma_no_stop_txt)
 
        return clean_txt

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

clean_corpus = [process_text(sentence) for sentence in tqdm(some_sent) if sentence.strip() !='']
 
word_tokenizer = nltk.WordPunctTokenizer()
word_tokens = [word_tokenizer.tokenize(sent) for sent in tqdm(clean_corpus)]
word_tokens