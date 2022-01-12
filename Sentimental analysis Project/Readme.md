# SENTIMENTAL ANALYSIS OF AMAZON CUSTOMER REVIEWS

### Introduction
Understanding a customer is the most vital part for every business, as it helps them to find out their needs, build relationship,  build better products and make profits. However, manual sentiment analysis of each customer is a cumbersome process.But Nowadays, many organizations are incorporating sentiment analysis using AI into their business, to get better insights and automate the process. In this end to end project, I have collected the reviews of different products by amazon customers and  leveraged natural language processing techniques to build classifiers to classify sentiment(positive or negative) of customer towards product.

### Methods Used
- Web scraping
- Text Classification
- Machine Learning
- Deep Learning

### Tools and Libraries
- Python
- Pandas, Numpy, beautifulsoup, nltk, Sklearn, and Keras
- Jupyter IDE

### Project Flow
<b>1) Data Collection</b> 
  - Webscraped the ratings and reviews of customers from consumeraffairs.com using beautifulsoup Library. https://www.consumeraffairs.com/online/amazon.html

<b>2) Data Preprocessing</b> 
  - Pre-processed the web scraped data by removing unwanted statements using pandas library. 
  - Labelled reviews with 2 classes based on ratings.
  - file: Sentimental analysis (webscraping and preprocessing).py

<b>3) Text Vectorization</b> 
-  Vectorized the text using Bag of words, TF-IDF and wordtovec(fasttext) techniques for machine learning models.

<b>4) Model training</b> 
  - Trained three ML algorithms(SVM, Naive Bayes and Logistic regression) on 2 word representation techniques(Bag of words and TF-IDF)
  - Files: Sentmental Analysis using count vectorizer.ipynb, Sentmental Analysis using TF-IDF.ipynb.
  - Performed Artificial neural network algorithm on bag of words word representations.
  - file: ANN.ipynb
  
  - Trained three DL algorithms(LSTM, GRU and Bi-Directional LSTM) on word to vec word representation(fasttext)
  - file: LSTM/GRU/Bi-DIRECT.ipynb
  
<b>5) Model Evaluation</b>
  - Performed comparative analysis
  
  ![image](https://user-images.githubusercontent.com/55615788/149210462-b0fb2199-9119-44ff-8637-f5dec73e2b5e.png)

<b>6) Deployment</b>
  - Deployed the trained model for customer review sentiment analysis using flask app. 
