from flask import Flask,render_template,url_for,request
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#import pandas as pd 
#from sklearn.externals import joblib
import pickle

# load the model from disk
clf = pickle.load(open('clf.pkl', 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

	if request.method == 'POST':
		review = request.form['message']
		#Data cleaning and preprocessing
		
		wordnet = WordNetLemmatizer()

		review = review.replace('$','dollars')
    
		# keeping only text and numbers in reviews
		review = re.sub('%', ' percent', review)
		review = re.sub('[^a-zA-Z0-9/]', ' ', review)
		review = review.lower()
		review = review.split()
    
		# Removing Stopwords
		review = [wordnet.lemmatize(word) for word in review if not word in stopwords.words('english')]
		review = ' '.join(review)

		data = [review]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)