# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:01:35 2021

@author: Vandan
"""

# Import libraries
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Modelling():

    
# ********************************************************************************************************************    
    # Data pre processing
    def Preprocessing():
        
        # Lemmatizer object
        wordnet = WordNetLemmatizer()
        
        # Drop unwanted columns
        data.drop('Unnamed: 0',axis=1,inplace=True)
        
        reviews =  []
        for i in range(0, len(data)):
            # Replacing values in rows
            review = data['Reviews'][i]
            review = review.replace('$','dollars')
    
            # keeping only text and numbers in reviews
            review = re.sub('%', ' percent', review)
            review = re.sub('[^a-zA-Z0-9/]', ' ', review)
            review = review.lower()
            review = review.split()
    
            # Removing Stopwords
            review = [wordnet.lemmatize(word) for word in review if not word in stopwords.words('english')]
            review = ' '.join(review)
    
            # appending into list
            reviews.append(review)
            
        reviews = pd.DataFrame(reviews)
        ratings = data['Ratings']
        
        # creating a complete data frame
        preprocessed_data = pd.concat([ratings,reviews],axis=1)
        preprocessed_data['Ratings','Reviews']
    
        return preprocessed_data
    
# ********************************************************************************************************************


# ********************************************************************************************************************
    # Function to perform Naive Bayes algorithm
    def Naive_Bayes(data):
        
        # Creating the Bag of Words model
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer(max_features=5000)
        X = cv.fit_transform(data['Reviews']).toarray()

        #dummyfying output variable
        y=pd.get_dummies(data['Ratings'],drop_first=True)
        
        # Train Test Split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)
        
        # Training model using Naive bayes classifier
        from sklearn.naive_bayes import MultinomialNB
        nb_model = MultinomialNB(alpha=0.01).fit(X_train, y_train)
        
        
        
        # Training Evaluation
        y_pred_t = nb_model.predict(X_train)

        # Classification metrics
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        cm_train = confusion_matrix(y_pred_t, y_train)
        
        print('NAIVE BAYES:')
        print('Training Evaluation')
        print("Confusion Matrix:")
        print(cm_train)

        report_train = classification_report(y_pred_t, y_train)
        print("Classification Report:",)
        print (report_train)

        accuracy_train = accuracy_score(y_pred_t,y_train)
        print("Accuracy:",accuracy_train)
        
        
        
        # Testing Evaluation Evaluation
        y_pred = nb_model.predict(X_test)

        # Classification metrics
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        cm_test = confusion_matrix(y_pred, y_test)
        print('')
        print('Training Evaluation')
        print("Confusion Matrix:")
        print(cm_test)

        report_test = classification_report(y_pred, y_test)
        print("Classification Report:",)
        print (report_test)

        accuracy_test = accuracy_score(y_pred,y_test)
        print("Accuracy:",accuracy_test)
    
# ********************************************************************************************************************    
    

# ********************************************************************************************************************    
    # Function to perform logistic regression
    def Logistic_Regresison():
        
        # Creating the Bag of Words model
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer(max_features=5000)
        X = cv.fit_transform(data['Reviews']).toarray()

        #dummyfying output variable
        y=pd.get_dummies(data['Ratings'],drop_first=True)
        
        # Train Test Split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)
        
        # Training model using Logistic regression
        from sklearn.linear_model import LogisticRegression
        log_model = LogisticRegression(solver= 'newton-cg', penalty= 'l2', C=0.1).fit(X_train, y_train)
        
        
        
        # Training Evaluation
        y_pred_t = log_model.predict(X_train)

        # Classification metrics
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        cm_train = confusion_matrix(y_pred_t, y_train)
        
        print('LOGISTIC REGRESSION:')
        print('Training Evaluation')
        print("Confusion Matrix:")
        print(cm_train)

        report_train = classification_report(y_pred_t, y_train)
        print("Classification Report:",)
        print (report_train)

        accuracy_train = accuracy_score(y_pred_t,y_train)
        print("Accuracy:",accuracy_train)
        
        
        
        # Testing Evaluation Evaluation
        y_pred = log_model.predict(X_test)

        # Classification metrics
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        cm_test = confusion_matrix(y_pred, y_test)
        print('')
        print('Training Evaluation')
        print("Confusion Matrix:")
        print(cm_test)

        report_test = classification_report(y_pred, y_test)
        print("Classification Report:",)
        print (report_test)

        accuracy_test = accuracy_score(y_pred,y_test)
        print("Accuracy:",accuracy_test)
        
# ********************************************************************************************************************        
        

# ********************************************************************************************************************        
    # Function to perform Support Vector Machine    
    def SVM():
        
        # Creating the Bag of Words model
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer(max_features=5000)
        X = cv.fit_transform(data['Reviews']).toarray()

        #dummyfying output variable
        y=pd.get_dummies(data['Ratings'],drop_first=True)
        
        # Train Test Split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)
        
        # Training model using Logistic regression
        from sklearn import svm
        svm_model = svm.SVC()
        svm_model.fit(X_train,y_train)
        
        
        # Training Evaluation
        y_pred_t = svm_model.predict(X_train)

        # Classification metrics
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        cm_train = confusion_matrix(y_pred_t, y_train)
        
        print('LOGISTIC REGRESSION:')
        print('Training Evaluation')
        print("Confusion Matrix:")
        print(cm_train)

        report_train = classification_report(y_pred_t, y_train)
        print("Classification Report:",)
        print (report_train)

        accuracy_train = accuracy_score(y_pred_t,y_train)
        print("Accuracy:",accuracy_train)
        
        
        
        # Testing Evaluation Evaluation
        y_pred = svm_model.predict(X_test)

        # Classification metrics
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        cm_test = confusion_matrix(y_pred, y_test)
        print('')
        print('Training Evaluation')
        print("Confusion Matrix:")
        print(cm_test)

        report_test = classification_report(y_pred, y_test)
        print("Classification Report:",)
        print (report_test)

        accuracy_test = accuracy_score(y_pred,y_test)
        print("Accuracy:",accuracy_test)

# ********************************************************************************************************************


# Creating an Object
model = Modelling()

# Read Data from CSV file        
data = pd.read_csv('Amazon_customer_Reviews.csv')

# Calling Preprocessing function        
preprocess = model.Preprocessing(data)

# Naive Bayes Algorithm
model.Naive_Bayes(preprocess)

# Logisistic Regression Algorithm
model.Logistic_Regression(preprocess)

# Support Vector Machine Algorithm
model.SVM(preprocess)