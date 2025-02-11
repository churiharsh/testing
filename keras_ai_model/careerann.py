# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 07:05:27 2022

@author: Abhishek
"""

# Artificial Neural Network

# Importing the libraries
import numpy as np
import pandas as pd
import tensorflow as tf
import os.path as op
import sys 


#---Data Preprocessing------

# Importing the dataset
dataset = pd.read_csv('../keras_ai_model/data.csv')

#independent variable matrix upperbound exclusive hota hai!!
X = dataset.iloc[:, 0:19].values #pd illoc

#taking care of missing data(nan)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
#fitting our imputer obj to data 
imputer = imputer.fit(X[:,:])
#replacing the missing data
X[:,:] = imputer.transform(X[:,:])

#dependent variable matrix
y = dataset.iloc[:, -1].values



# Encoding categorical data
# Label Encoding column
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
le = LabelEncoder()
X[:, 1] = le.fit_transform(X[:, 1])

# Label Encoding column
#from sklearn.preprocessing import LabelEncoder
le_1 = LabelEncoder()
X[:, 2] = le_1.fit_transform(X[:, 2])

# Label Encoding column
le_2 = LabelEncoder()
X[:, 3] = le_2.fit_transform(X[:, 3])


# Label Encoding column
le_3 = LabelEncoder()
X[:, 4] = le_3.fit_transform(X[:, 4])


# Label Encoding column
le_4 = LabelEncoder()
X[:, 5] = le_4.fit_transform(X[:, 5])

# Label Encoding column
le_5 = LabelEncoder()
X[:, 6] = le_5.fit_transform(X[:, 6])


# Label Encoding column
le_6 = LabelEncoder()
X[:, 7] = le_6.fit_transform(X[:, 7])



# Label Encoding column
le_7 = LabelEncoder()
X[:, 8] = le_7.fit_transform(X[:, 8])

# Label Encoding column
le_8 = LabelEncoder()
X[:, 9] = le_8.fit_transform(X[:, 9])

# Label Encoding column
le_9 = LabelEncoder()
X[:, 10] = le_9.fit_transform(X[:, 10])

# Label Encoding column
le_10 = LabelEncoder()
X[:, 11] = le_10.fit_transform(X[:, 11])

# Label Encoding column
le_11 = LabelEncoder()
X[:, 12] = le_11.fit_transform(X[:, 12])

# Label Encoding column
le_12 = LabelEncoder()
X[:, 13] = le_12.fit_transform(X[:, 13])

# Label Encoding column
le_13 = LabelEncoder()
X[:, 14] = le_13.fit_transform(X[:, 14])

# Label Encoding column
le_14 = LabelEncoder()
X[:, 15] = le_14.fit_transform(X[:, 15])


# Label Encoding column
le_15 = LabelEncoder()
X[:, 16] = le_15.fit_transform(X[:, 16])

# Label Encoding column
le_16 = LabelEncoder()
X[:, 17] = le_16.fit_transform(X[:, 17])


# Label Encoding column
le_17 = LabelEncoder()
X[:, 18] = le_17.fit_transform(X[:, 18])



#dummy variable encoding
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [3])],   # The column numbers to be transformed 
    remainder='passthrough'                                         # Leave the rest of the columns untouched
)

X = ct.fit_transform(X)


#removing one dummy to avoid dummy variable trap
X = X[:,1:]


#label encoding the dependent col
le_y = LabelEncoder()
y = le_y.fit_transform(y)
y_bef = y

#dummy encoding
onehotencoder = OneHotEncoder(categories='auto')
y = onehotencoder.fit_transform(y.reshape(-1,1)).toarray()
#dummy trap removal
y = y[:,1:]



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#--------end of data preprocessing--------------------


#----------------------------- Building the ANN----------------------

# Initializing the ANN
ann = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer
ann.add(tf.keras.layers.Dense(units=15, activation='relu'))

#adding dropout temp rahega
#ann.add(tf.keras.layers.Dropout(.1))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=15, activation='relu'))

# Adding the output layer 
#softmx regression
ann.add(tf.keras.layers.Dense(units=9, activation='softmax'))


# Compiling the ANN
ann.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Training the ANN on the Training set
ann.fit(X_train, y_train, batch_size = 10, epochs = 100)

# Predicting the Test set results
y_pred = ann.predict(X_test)
y_pred = (y_pred >0.5)


#making confusion matrix
from sklearn.metrics import multilabel_confusion_matrix
cm = multilabel_confusion_matrix(y_test,y_pred)

in_dat = np.asarray([sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],
                sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19],sys.argv[20]])
tf.constant(in_dat)
print(in_dat)

single_pred = ann.predict(sc.transform([in_dat]))

single_pred = (single_pred > 0.2)

print(single_pred)

    
    