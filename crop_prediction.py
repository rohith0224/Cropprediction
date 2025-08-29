import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data= pd.read_csv("Crop_recommendation.csv")


X=data.iloc[:,:-1]
Y=data.iloc[:,-1]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

model= RandomForestClassifier()

model.fit(X_train,Y_train)


pickle.dump(model,open('crop_recommendation_model.pkl','wb'))