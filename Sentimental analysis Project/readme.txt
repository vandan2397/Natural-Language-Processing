<h2>SENTIMENTAL ANALYSIS OF AMAZON CUSTOMER REVIEWS</h2>

Understanding a customer is the most vital part for every business, as it helps them to find out their needs, build relationship,  build better products and make profits. However, manual sentiment analysis of each customer is a cumbersome process.But Nowadays, many organizations are incorporating sentiment analysis using AI into their business, to get better insights and automate the process. In this end to end project, I have collected the reviews of products by amazon customers and  leveraged natural language processing techniques to build classifiers to classify sentiment(positive or negative). Following are the detailed steps of the project:

1) Data Collection and Preprocessing 
  -> Webscraped the ratings and reviews of customers from consumeraffairs.com using beautifulsoup Library
  -> Pre-processed the web scraped data by removing unwanted statements using pandas library.
  -> Labelled ratings with class.
  -> file: Sentimental analysis (webscraping and preprocessing).py

2) Model training 
  -> Performed three ML algorithms(SVM, Naive Bayes and Logistic regression) on two different word representations(Bag of words and TF-IDF) using sklearn and nltk library.
  -> files: Sentmental Analysis using count vectorizer.ipynb, Sentmental Analysis using TF-IDF.ipynb
  
  -> Performed Artificial neural network algorithm on bag of words word representations
  -> file: ANN.ipynb
  
  -> Performed three DL algorithms(LSTM, GRU and Bi-Directional LSTM) on word to vec word representations(fasttext)
  -> file: LSTM/GRU/Bi-DIRECT.ipynb
  
3) Model Evaluation
  -> Model Evaluation.xlsx file contains results of all models.
  -> Performed comparative analysis
  
4) Deployment
  -> Deployment folder contains deployment code for customer review sentiment analysis using flask app.   
 
