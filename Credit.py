import pandas as pd
import numpy as np

# Data processing

df = pd.read_csv('/content/credit_data.csv')
df.head()
df.value_counts('Class')
df.info()
df.isnull().sum()

# Under sampling

df_legit = df[df.Class == 0]
df_fraud = df[df.Class == 1]
df_sample = pd.concat([legit_sample, fraud_sample], axis=0)
df_sample.head()
df_sample.isnull().sum()

# Model Traing

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
  X = df_sample.drop(columns='Class', axis=1)
  Y = df_sample['Class']
print(X)
print(Y)
print(type(Y))

#Spliting the dataset

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=3)

print(X)
print(X_train)
print(X_test)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

model = LogisticRegression()
model.fit(X_train,Y_train)

model.score(X_train,Y_train)
model.score(X_test,Y_test)
pre = model.predict(X_test)
accuracy_score(pre,Y_test)

input_data = (10,1.44904378114715,-1.17633882535966,0.913859832832795,-1.37566665499943,-1.97138316545323,-0.62915213889734,-1.4232356010359,0.0484558879088564,-1.72040839292037,1.62665905834133,1.1996439495421,-0.671439778462005,-0.513947152539479,-0.0950450453999549,0.230930409124119,0.0319674667862076,0.253414715863197,0.854343814324194,-0.221365413645481,-0.387226474431156,-0.00930189652490052,0.313894410791098,0.0277401580170247,0.500512287104917,0.25136735874921,-0.129477953726618,0.0428498709381461,0.0162532619375515,7.8,)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)
prediction = model.predict(input_data)

print(prediction[0])

if prediction[0] == 0:
  print('Legit')
else:
  print('Fraud')
