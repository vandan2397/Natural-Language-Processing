# SENTIMENTAL ANALYSIS OF AMAZON CUSTOMER REVIEWS

### Introduction
Understanding a customer is the most vital part for every business, as it helps them to find out their needs, build relationship,  build better products and make profits. However, manual sentiment analysis of each customer is a cumbersome process.But Nowadays, many organizations are incorporating sentiment analysis using AI into their business, to get better insights over what customers think of product, maintain public perception and automate the process. In this end to end project, I have collected the reviews of different products by amazon customers and  leveraged natural language processing techniques to build classifiers to classify sentiment(positive or negative) of customer towards product.

### Methods Used
- Web scraping
- Text Pre-Processing
- Text Classification
- Machine Learning
- Deep Learning

### Tools and Libraries
- Python
- Pandas, Numpy, beautifulsoup, nltk, Sklearn, and Keras
- Google Colab

### Project Flow
<b>1) Data Collection and Labelling</b> 
  - Webscraped the ratings and reviews of customers from consumeraffairs.com using beautifulsoup Library.
  - Labelled reviews with 2 classes based on ratings.
  - https://www.consumeraffairs.com/online/amazon.html
  - File: 1. Webscraping and labelling.ipynb

<b>2) Data Preprocessing</b> 
  - Pre-processed the web scraped data by removing unwanted statements using pandas library.
  - Removed Special characters (kept only numbers and alphabets)
  - Lowercased all reviews
  - Perfomed lemmatization
  - File: 2. Pre-Processing.ipynb

<b>3) Exploratory Data Analysis</b> 
  -  Performed exploratory data analysis of reviews to understand what are the frequent topics customers talking about.
  -  File: 3. Exploratory Data Analysis.ipynb

<b>4) Text Vectorization</b> 
  -  Vectorized the text using Bag of words, TF-IDF and wordtovec(fasttext) techniques for machine learning models.

<b>5) Model training</b> 
  - Trained 3 Machine Learning algorithms(SVM, Naive Bayes and Logistic regression) on 2 word representation techniques(Bag of words and TF-IDF)
  - Trained 2 Deep Learning algorithms(LSTM, Bi-Directional LSTM) on word to vec word representation(fasttext)
  - Files: 4. Model Training (Logistic Regression, Naive Bayes, SVM) with Bag of Words.ipynb, 5. Model Training (Logistic Regression, Naive Bayes, SVM) with TF-    IDF.ipynb, 6. Model Training (LSTM and Bi-LSTM) with Word to Vec.ipynb
  
<b>6) Model training</b> 
  - Performed Hyperparameter tuning on Naive bayes with N-Gram to improve performance.
  
<b>7) Model Evaluation</b>
  - Performed comparative analysis
  ![image](https://github.com/vandan2397/Natural-Language-Processing/assets/55615788/a2c002d1-7a7a-4e1d-a6b0-1a9590f55487)

  
  
  - Analysis shows BI-LSTM with wordtovec outperforms all other algorithms in terms of accuracy and F1 Score.

<b>7) Deployment</b>
  - Deployed the trained model for customer review sentiment analysis using flask app. 
