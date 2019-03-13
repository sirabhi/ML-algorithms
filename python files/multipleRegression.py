# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:06:37 2018

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset=pd.read_csv('50_Startups.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,4].values

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3])
onehotencoder=OneHotEncoder(categorical_features = [3])
X=onehotencoder.fit_transform(X).toarray()

#Avoiding Dummy variable trap
X=X[:,1:]



#splitting data set into training set and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)

#Feature scalling
""""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)"""

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
#train 
regressor.fit(X_train,Y_train)
#Predicting The Test set results
Y_pred=regressor.predict(X_test)

#Building the optimal model using Backward Eleminattion
#that taking most important attributes than others
import statsmodels.formula.api as sm
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
#here what we doing is creating a new coumn filled with ones because 
#in for formula y=b0+b1x1+b2x2 ......
#linear regression library automatically understands b0x0 where b0=1
#but here we are using stasmodel library for backward elemination which do not understands the b0x0
#so we have to manualy append it 

#fit the whole model with all pridictors
X_opt=X[:,[0,1,2,3,4,5]]

regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()
#see the p values and remove the attribute which having highest p value
#fit the model without that attribute

X_opt=X[:,[0,1,3,4,5]]

regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

X_opt=X[:,[0,3,4,5]]

regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

X_opt=X[:,[0,3,5]]

regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()

X_opt=X[:,[0,3]]

regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()




